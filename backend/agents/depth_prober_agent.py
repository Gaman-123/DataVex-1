import json
from core.groq_client import chat
from models.types import Track

SYSTEM = """You are DepthProberAgent. Generate surgical follow-up questions.
Reference exactly what the candidate said. Feel like a conversation, not interrogation.
Return ONLY valid JSON."""

STYLES = {
    Track.conceptual:   {"follow_up":"Target the exact gap. Reference their words.","stress_test":"Push to production scale or adversarial conditions."},
    Track.lc:           {"follow_up":"Ask to optimize or handle a missed edge case.","stress_test":"Introduce a constraint that breaks their approach."},
    Track.realworld:    {"follow_up":"Ask for specific numbers, names — prove they lived it.","stress_test":"Scale to 100x traffic, 3am incident, team conflict."},
    Track.resume_drill: {"follow_up":"Ask for the specific detail proving the claim.","stress_test":"Present contradiction between what they said vs resume."},
}

async def run_depth_prober(
    track: Track,
    original_question: str,
    candidate_answer: str,
    evaluator_signals: dict,
    probe_trigger: str,
    requisite_skill: str,
) -> dict:

    style = STYLES[track][probe_trigger]

    msg = f"""
TRACK: {track.value}
PROBE TYPE: {probe_trigger}
STYLE: {style}
REQUISITE SKILL: {requisite_skill}

ORIGINAL QUESTION: {original_question}
CANDIDATE SAID: {candidate_answer}
EVALUATOR FOUND: {json.dumps(evaluator_signals, indent=2)}

Return JSON:
{{
  "probe_question": "exact follow-up to ask",
  "probe_type": "{probe_trigger}",
  "targets": "what gap or strength this probes",
  "requisite_skill": "{requisite_skill}",
  "expected_good_answer": "what strong candidate says",
  "red_flag_answer": "what bluffing candidate says"
}}
"""
    raw = await chat(
        messages=[{"role":"system","content":SYSTEM},{"role":"user","content":msg}],
        model="smart", temperature=0.5, json_mode=True
    )
    return json.loads(raw)