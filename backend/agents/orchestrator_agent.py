import json
from core.groq_client import chat
from models.types import OrchestratorOutput

SYSTEM = """You are OrchestratorAgent — the interview brain.
Ensure every HR must-have skill reaches required depth before session ends.
Enforce requisite coverage. Manage time and track switching.
Return ONLY valid JSON."""

async def run_orchestrator(
    session_state: dict,
    evaluator_output: dict,
    voice_output: dict,
    requirements: dict,
    question_plan: dict,
) -> OrchestratorOutput:

    must_haves  = [s["skill"] for s in requirements.get("must_have_skills", [])]
    coverage    = session_state.get("requisite_coverage", {})
    uncovered   = [s for s in must_haves if coverage.get(s,"uncovered") in ["uncovered","surface"]]
    time_left   = session_state["time_budget_seconds"] - session_state["time_elapsed_seconds"]
    time_pct    = (time_left / session_state["time_budget_seconds"]) * 100

    msg = f"""
SESSION:
- questions_asked: {session_state.get('questions_asked',0)}
- time_remaining_pct: {time_pct:.0f}%
- current_track: {session_state.get('current_track')}
- track_time_used: {json.dumps(session_state.get('track_time_used',{}))}

REQUISITE COVERAGE: {json.dumps(coverage)}
UNCOVERED MUST-HAVES: {uncovered}

LAST EVALUATOR: {json.dumps(evaluator_output)}
LAST VOICE: {json.dumps(voice_output)}

RULES:
1. time_remaining < 15% AND uncovered must-haves → force direct probe, override track
2. next_action is follow_up or stress_test → stay on current question
3. misalignment_flag=true AND bluffing → switch to resume_drill
4. lc track > 30% budget used → switch track
5. all must-haves deep/exceeded → can close

Return JSON:
{{
  "next_action": "follow_up|stress_test|next_question|switch_track|close",
  "next_track": "conceptual|lc|realworld|resume_drill|null",
  "next_question": "question text or null",
  "hr_nudge": "short live tip for HR interviewer",
  "requisite_alert": "warning if must-have at risk or null"
}}
"""
    raw = await chat(
        messages=[{"role":"system","content":SYSTEM},{"role":"user","content":msg}],
        model="fast", temperature=0.2, json_mode=True
    )
    return OrchestratorOutput(**json.loads(raw))