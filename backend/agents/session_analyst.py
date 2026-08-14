import json
from core.groq_client import chat

SYSTEM = """You are SessionAnalystAgent — the final decision maker.
Synthesize all interview rounds. Every claim must reference a specific round ID.
Produce an evidence-based hire recommendation.
Return ONLY valid JSON."""

async def run_session_analyst(
    requirements: dict,
    candidate: dict,
    all_rounds: list[dict],
    requisite_coverage: dict,
) -> dict:

    msg = f"""
REQUIREMENTS:
{json.dumps(requirements, indent=2)}

CANDIDATE: {candidate.get('full_name')} | College: {candidate.get('college','?')} | fit_score: {candidate.get('fit_score')}

FINAL REQUISITE COVERAGE:
{json.dumps(requisite_coverage, indent=2)}

ALL ROUNDS ({len(all_rounds)} total):
{json.dumps(all_rounds, indent=2)}

Return JSON:
{{
  "hire_signal": "strong_yes|yes|lean_yes|lean_no|no",
  "overall_score": 0.0-1.0,
  "conceptual_score": 0.0-1.0,
  "lc_score": 0.0-1.0,
  "rw_score": 0.0-1.0,
  "resume_drill_score": 0.0-1.0,
  "voice_confidence_avg": 0.0-10.0,
  "requisite_coverage_report": {{
    "SkillName": {{"level":"not_assessed|surface|partial|deep|exceeded","evidence":"round X showed...","meets_requisite":true}}
  }},
  "uncovered_dealbreakers": [],
  "lc_report": {{
    "problems_attempted": 0,
    "max_difficulty_reached": "easy|medium|hard",
    "complexity_awareness_score": 0.0-1.0,
    "memorized_vs_understood": "memorized|mixed|understood",
    "summary": "..."
  }},
  "rw_report": {{
    "scenarios_handled": 0,
    "production_thinking_score": 0.0-1.0,
    "failure_honesty_index": 0.0-1.0,
    "tradeoff_quality_score": 0.0-1.0,
    "summary": "..."
  }},
  "voice_report": {{
    "confidence_trajectory": "declining|stable|improving",
    "misalignment_moments": [],
    "key_hesitation_terms": []
  }},
  "standout_moments": [{{"round_id":"x","moment":"..."}}],
  "red_flags": [{{"round_id":"x","flag":"..."}}],
  "onboarding_focus_areas": [],
  "full_reasoning": "3-5 sentence narrative"
}}
"""
    raw = await chat(
        messages=[{"role":"system","content":SYSTEM},{"role":"user","content":msg}],
        model="smart", temperature=0.2, max_tokens=4096, json_mode=True
    )
    return json.loads(raw)
