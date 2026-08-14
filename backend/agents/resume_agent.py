import json
from core.groq_client import chat
from models.types import CompanyRequirements, ResumeAnalysis

SYSTEM = """You are ResumeAgent — a senior technical recruiter AI.
Analyze the resume against company requirements.
Be critical. Skills with no project evidence = unproven.
Return ONLY valid JSON."""

async def run_resume_agent(resume_text: str, req: CompanyRequirements) -> ResumeAnalysis:
    msg = f"""
COMPANY REQUIREMENTS:
{req.model_dump_json(indent=2)}

CANDIDATE RESUME:
{resume_text}

Return JSON exactly:
{{
  "fit_score": 0.0-1.0,
  "missing_skills": ["skills required but absent or unproven"],
  "unproven_claims": ["claimed but no project proof"],
  "attack_vectors": [
    {{"skill":"X","angle":"why suspicious","probe_type":"depth","requisite_skill":"X"}}
  ],
  "lc_topic_hints": ["arrays","trees","dp"],
  "rw_scenario_seeds": [
    {{"project":"project name from resume","scenario_type":"scale|debug|incident|tradeoff","prompt":"scenario question"}}
  ],
  "dealbreaker_flags": ["triggered dealbreaker or empty"],
  "summary": "2-3 sentence assessment"
}}
"""
    raw = await chat(
        messages=[{"role":"system","content":SYSTEM},{"role":"user","content":msg}],
        model="smart", temperature=0.2, json_mode=True
    )
    return ResumeAnalysis(**json.loads(raw))