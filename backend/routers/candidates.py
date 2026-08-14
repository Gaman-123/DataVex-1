from fastapi import APIRouter, HTTPException
from core.supabase_client import supabase
from models.schemas import CandidateCreate
from models.types import CompanyRequirements
from agents.resume_agent import run_resume_agent

router = APIRouter(prefix="/candidates", tags=["candidates"])

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
async def create_candidate(data: CandidateCreate):
    req_res = (
        supabase.table("company_requirements")
        .select("*").eq("company_id", data.company_id)
        .eq("is_active", True).limit(1).execute()
    )
    if not req_res.data:
        raise HTTPException(400, "No active requirements for company")

    req = _build_req(req_res.data[0])
    analysis = await run_resume_agent(data.resume_raw_text, req)

    status = "rejected_pre" if analysis.dealbreaker_flags else "screened"

    payload = {
        **data.model_dump(),
        "fit_score":         analysis.fit_score,
        "missing_skills":    analysis.missing_skills,
        "unproven_claims":   analysis.unproven_claims,
        "attack_vectors":    analysis.attack_vectors,
        "lc_topic_hints":    analysis.lc_topic_hints,
        "rw_scenario_seeds": analysis.rw_scenario_seeds,
        "dealbreaker_flags": analysis.dealbreaker_flags,
        "resume_analysis":   {"summary": analysis.summary},
        "status":            status,
    }
    res = supabase.table("candidates").insert(payload).execute()
    return {"candidate": res.data[0], "analysis": analysis.model_dump(), "can_proceed": status != "rejected_pre"}

@router.get("/{candidate_id}")
async def get_candidate(candidate_id: str):
    res = supabase.table("candidates").select("*").eq("id", candidate_id).execute()
    if not res.data:
        raise HTTPException(404, "Not found")
    return res.data[0]

@router.get("/company/{company_id}")
async def list_candidates(company_id: str):
    res = (
        supabase.table("candidates")
        .select("id,full_name,email,college,fit_score,status,created_at")
        .eq("company_id", company_id).order("created_at", desc=True).execute()
    )
    return res.data