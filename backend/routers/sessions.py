from fastapi import APIRouter, HTTPException, WebSocket, WebSocketDisconnect
from core.supabase_client import supabase
from core.websocket_manager import ws_manager
from models.schemas import SessionCreate, AnswerSubmit, HROverride
from models.types import CompanyRequirements, Track
from agents.question_architect import run_question_architect
from agents.evaluator_agent import run_evaluator
from agents.voice_confidence_agent import run_voice_confidence
from agents.depth_prober_agent import run_depth_prober
from agents.orchestrator_agent import run_orchestrator
from agents.session_analyst import run_session_analyst
from agents.resume_agent import ResumeAnalysis
import asyncio, json
import logging, time

router = APIRouter(prefix="/sessions", tags=["sessions"])

logger = logging.getLogger("interviewai.sessions")
if not logger.handlers:
    handler = logging.StreamHandler()
    fmt = "%(asctime)s %(levelname)s [sessions] %(message)s"
    handler.setFormatter(logging.Formatter(fmt))
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

def _build_req(r: dict) -> CompanyRequirements:
    return CompanyRequirements(
        role_name=r["role_name"], role_level=r["role_level"],
        must_have_skills=r["must_have_skills"],
        nice_to_have_skills=r.get("nice_to_have_skills",[]),
        dealbreakers=r.get("dealbreakers",[]),
        evaluation_weights=r.get("evaluation_weights",{}),
        min_project_proof=r.get("min_project_proof",1),
        recency_window_months=r.get("recency_window_months",24),
        red_flag_patterns=r.get("red_flag_patterns",[]),
        enable_lc_rounds=r.get("enable_lc_rounds",True),
        lc_difficulty_cap=r.get("lc_difficulty_cap","med_allowed"),
        enable_rw_scenarios=r.get("enable_rw_scenarios",True),
        rw_depth=r.get("rw_depth","mid_level"),
    )

@router.post("/")
async def create_session(data: SessionCreate):
    c_res = supabase.table("candidates").select("*").eq("id", data.candidate_id).execute()
    r_res = supabase.table("company_requirements").select("*").eq("id", data.requirements_id).execute()
    if not c_res.data or not r_res.data:
        raise HTTPException(404, "Candidate or requirements not found")

    candidate = c_res.data[0]
    req_data  = r_res.data[0]
    req       = _build_req(req_data)

    analysis = ResumeAnalysis(
        fit_score=candidate["fit_score"] or 0,
        missing_skills=candidate.get("missing_skills",[]),
        unproven_claims=candidate.get("unproven_claims",[]),
        attack_vectors=candidate.get("attack_vectors",[]),
        lc_topic_hints=candidate.get("lc_topic_hints",[]),
        rw_scenario_seeds=candidate.get("rw_scenario_seeds",[]),
        dealbreaker_flags=candidate.get("dealbreaker_flags",[]),
        summary=candidate.get("resume_analysis",{}).get("summary",""),
    )

    plan = await run_question_architect(req, analysis)

    init_coverage = {s["skill"]: "uncovered" for s in req.must_have_skills}

    session_payload = {
        "candidate_id":       data.candidate_id,
        "company_id":         data.company_id,
        "hr_user_id":         data.hr_user_id,
        "requirements_id":    data.requirements_id,
        "status":             "planned",
        "question_plan":      plan,
        "current_track":      "track1_conceptual",
        "questions_asked":    0,
        "time_budget_seconds": 3600,
        "time_elapsed_seconds": 0,
        "requisite_coverage": init_coverage,
        "track_time_used":    {"track1":0,"track2":0,"track3":0,"track4":0},
    }

    s_res = supabase.table("interview_sessions").insert(session_payload).execute()
    return {"session": s_res.data[0], "question_plan": plan, "opening_question": plan.get("opening_question")}

@router.post("/start/{session_id}")
async def start_session(session_id: str):
    supabase.table("interview_sessions").update(
        {"status": "active", "started_at": "now()"}
    ).eq("id", session_id).execute()
    return {"status": "active"}

@router.post("/answer")
async def submit_answer(data: AnswerSubmit):
    # Load session
    s_res = supabase.table("interview_sessions").select("*").eq("id", data.session_id).execute()
    if not s_res.data:
        raise HTTPException(404, "Session not found")
    session = s_res.data[0]

    req_res = supabase.table("company_requirements").select("*").eq("id", session["requirements_id"]).execute()
    req_data = req_res.data[0]

    track = Track(data.track)

    # Run Agent 3 + Agent 4 in parallel (start as tasks so we can log timing)
    logger.info("Starting evaluator and voice confidence tasks for session=%s round=%s", data.session_id, data.round_number)
    t0 = time.perf_counter()
    evaluator_task = asyncio.create_task(run_evaluator(
        track, data.question_metadata, data.answer_transcript,
        data.answer_code, session.get("requisite_coverage", {})
    ))
    voice_task = asyncio.create_task(run_voice_confidence(
        track, data.question_text, data.answer_transcript, data.audio_features
    ))
    eval_out, voice_out = await asyncio.gather(evaluator_task, voice_task)
    t1 = time.perf_counter()
    logger.info("Evaluator finished (next_action=%s) and Voice finished (misalignment=%s) in %.3fs for session=%s round=%s",
                getattr(eval_out, 'next_action', None), getattr(voice_out, 'misalignment_flag', None), (t1 - t0), data.session_id, data.round_number)

    # Agent 5 — conditionally
    probe = None
    if getattr(eval_out, 'next_action', None) in ["follow_up", "stress_test"]:
        logger.info("DepthProber triggered for session=%s round=%s by evaluator.next_action=%s", data.session_id, data.round_number, eval_out.next_action)
        t_probe_start = time.perf_counter()
        probe = await run_depth_prober(
            track, data.question_text, data.answer_transcript,
            eval_out.signals, eval_out.next_action,
            data.requisite_skill or ""
        )
        t_probe_end = time.perf_counter()
        logger.info("DepthProber completed in %.3fs for session=%s round=%s", (t_probe_end - t_probe_start), data.session_id, data.round_number)

    # Update requisite coverage
    coverage = session.get("requisite_coverage", {})
    if eval_out.requisite_skill_updated:
        coverage[eval_out.requisite_skill_updated] = eval_out.requisite_new_level

    # Agent 6 (Orchestrator)
    session["requisite_coverage"] = coverage
    session["questions_asked"]    = session.get("questions_asked", 0) + 1
    logger.info("Starting orchestrator for session=%s round=%s", data.session_id, data.round_number)
    t_orch0 = time.perf_counter()
    orch = await run_orchestrator(session, eval_out.model_dump(), voice_out.model_dump(), req_data, session["question_plan"])
    t_orch1 = time.perf_counter()
    logger.info("Orchestrator decided next_action=%s next_track=%s in %.3fs for session=%s round=%s", orch.next_action, orch.next_track, (t_orch1 - t_orch0), data.session_id, data.round_number)

    # Save round
    round_payload = {
        "session_id":           data.session_id,
        "round_number":         data.round_number,
        "track":                data.track,
        "requisite_skill":      data.requisite_skill,
        "question_text":        data.question_text,
        "question_metadata":    data.question_metadata,
        "answer_transcript":    data.answer_transcript,
        "answer_code":          data.answer_code,
        "audio_features":       data.audio_features,
        "understanding_level":  eval_out.understanding_level,
        "content_score":        eval_out.content_score,
        "next_action":          eval_out.next_action,
        "evaluator_signals":    eval_out.signals,
        "requisite_updated_to": eval_out.requisite_new_level,
        "confidence_level":     voice_out.confidence_level,
        "hesitation_map":       voice_out.hesitation_map,
        "misalignment_flag":    voice_out.misalignment_flag,
        "misalignment_type":    voice_out.misalignment_type,
        "probe_generated":      probe is not None,
        "probe_question":       probe["probe_question"] if probe else None,
    }
    supabase.table("interview_rounds").insert(round_payload).execute()

    # Update session
    supabase.table("interview_sessions").update({
        "requisite_coverage": coverage,
        "questions_asked":    session["questions_asked"],
        "current_track":      orch.next_track or session.get("current_track"),
    }).eq("id", data.session_id).execute()

    # Push to WebSocket
    ws_payload = {
        "type":              "round_complete",
        "understanding":     eval_out.understanding_level,
        "content_score":     eval_out.content_score,
        "confidence":        voice_out.confidence_level,
        "misalignment":      voice_out.misalignment_flag,
        "misalignment_type": voice_out.misalignment_type,
        "next_action":       orch.next_action,
        "next_track":        orch.next_track,
        "next_question":     orch.next_question or (probe["probe_question"] if probe else None),
        "hr_nudge":          orch.hr_nudge,
        "requisite_alert":   orch.requisite_alert,
        "coverage":          coverage,
    }
    await ws_manager.send(data.session_id, ws_payload)

    return ws_payload

@router.post("/close/{session_id}")
async def close_session(session_id: str):
    s_res = supabase.table("interview_sessions").select("*").eq("id", session_id).execute()
    session   = s_res.data[0]
    c_res     = supabase.table("candidates").select("*").eq("id", session["candidate_id"]).execute()
    req_res   = supabase.table("company_requirements").select("*").eq("id", session["requirements_id"]).execute()
    rounds_res = supabase.table("interview_rounds").select("*").eq("session_id", session_id).execute()

    report = await run_session_analyst(
        req_res.data[0], c_res.data[0],
        rounds_res.data, session.get("requisite_coverage", {})
    )

    supabase.table("interview_sessions").update({
        "status": "completed", "hire_signal": report["hire_signal"],
        "final_report": report, "ended_at": "now()"
    }).eq("id", session_id).execute()

    supabase.table("session_reports").insert({
        "session_id":               session_id,
        "candidate_id":             session["candidate_id"],
        "company_id":               session["company_id"],
        "college":                  c_res.data[0].get("college"),
        "hire_signal":              report["hire_signal"],
        "overall_score":            report["overall_score"],
        "conceptual_score":         report["conceptual_score"],
        "lc_score":                 report["lc_score"],
        "rw_score":                 report["rw_score"],
        "resume_drill_score":       report["resume_drill_score"],
        "voice_confidence_avg":     report["voice_confidence_avg"],
        "requisite_coverage_report":report["requisite_coverage_report"],
        "uncovered_dealbreakers":   report["uncovered_dealbreakers"],
        "lc_report":                report["lc_report"],
        "rw_report":                report["rw_report"],
        "voice_report":             report["voice_report"],
        "standout_moments":         report["standout_moments"],
        "red_flags":                report["red_flags"],
        "onboarding_focus_areas":   report["onboarding_focus_areas"],
        "full_reasoning":           report["full_reasoning"],
    }).execute()

    await ws_manager.send(session_id, {"type": "session_closed", "report": report})
    return report

@router.websocket("/ws/{session_id}")
async def websocket_endpoint(websocket: WebSocket, session_id: str):
    await ws_manager.connect(session_id, websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        ws_manager.disconnect(session_id)

@router.get("/{session_id}")
async def get_session(session_id: str):
    res = supabase.table("interview_sessions").select("*").eq("id", session_id).execute()
    if not res.data:
        raise HTTPException(404, "Session not found")
    return res.data[0]