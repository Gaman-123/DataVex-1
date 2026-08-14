import json
from core.groq_client import chat
from models.types import EvaluatorOutput, Track

SYSTEM = """You are EvaluatorAgent. Score candidate answers strictly.
Buzzwords without substance = low score. Real depth = high score.
You are track-aware. Return ONLY valid JSON."""

TRACK_FOCUS = {
    Track.conceptual:   "depth_markers, buzzword_density(penalize), understanding_vs_memorized",
    Track.lc:           "correct, time_complexity_stated, edge_cases_handled, narrated_while_coding, brute_force_only(penalize)",
    Track.realworld:    "structured_thinking, failure_honesty, scale_awareness, trade_off_depth, specificity",
    Track.resume_drill: "claim_verified, specific_numbers_given, contradiction_detected(penalize), vague_answer(penalize)",
}

async def run_evaluator(
    track: Track,
    question: dict,
    answer_transcript: str,
    answer_code: str | None,
    requisite_coverage: dict,
) -> EvaluatorOutput:

    code_section = f"\nCANDIDATE CODE:\n{answer_code}" if answer_code else ""

    msg = f"""
TRACK: {track.value}
SCORING FOCUS: {TRACK_FOCUS[track]}

QUESTION:
{json.dumps(question, indent=2)}

TRANSCRIPT: {answer_transcript}
{code_section}

CURRENT REQUISITE COVERAGE:
{json.dumps(requisite_coverage, indent=2)}

Return JSON:
{{
  "understanding_level": "surface|partial|deep|exceeded",
  "content_score": 0.0-1.0,
  "next_action": "follow_up|stress_test|next_question|switch_track|close",
  "signals": {{"finding":"detail"}},
  "requisite_skill_updated": "skill name",
  "requisite_new_level": "surface|partial|deep|exceeded",
  "reasoning": "1-2 sentences"
}}
"""
    raw = await chat(
        messages=[{"role":"system","content":SYSTEM},{"role":"user","content":msg}],
        model="fast", temperature=0.1, json_mode=True
    )
    return EvaluatorOutput(**json.loads(raw))