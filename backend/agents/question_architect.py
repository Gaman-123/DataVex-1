import json
from core.groq_client import chat
from models.types import CompanyRequirements, ResumeAnalysis

SYSTEM = """You are QuestionArchitectAgent.
Build a 4-track interview plan. Every question maps to an HR requisite skill.
Never ask "what is X". Always probe understanding, not definitions.
Return ONLY valid JSON."""

async def run_question_architect(req: CompanyRequirements, analysis: ResumeAnalysis) -> dict:
    diff = {"junior":"easy","mid":"easy_to_medium","senior":"medium_to_hard","staff":"hard"}
    starting = diff.get(req.role_level, "medium")

    msg = f"""
REQUIREMENTS:
{req.model_dump_json(indent=2)}

RESUME ANALYSIS:
{analysis.model_dump_json(indent=2)}

Build the 4-track plan. Return JSON:
{{
  "track1_conceptual": [
    {{
      "id": "c1",
      "requisite_skill": "Python",
      "question": "...",
      "type": "opener",
      "green_flags": ["..."],
      "red_flags": ["..."],
      "follow_up": "...",
      "stress_test": "..."
    }}
  ],
  "track2_lc": [
    {{
      "id": "lc1",
      "requisite_skill": "Python",
      "topic": "hashmaps",
      "difficulty": "{starting}",
      "problem_title": "Two Sum",
      "problem_statement": "...",
      "constraints": "...",
      "example_input": "...",
      "example_output": "...",
      "optimal_approach": "hashmap O(n)",
      "time_limit_minutes": 20,
      "eval_checklist": ["correct","stated complexity","edge cases","narrated"]
    }}
  ],
  "track3_rw": [
    {{
      "id": "rw1",
      "requisite_skill": "System Design",
      "seed_project": "from resume",
      "scenario_type": "debugging|scale|incident|tradeoff",
      "surface_prompt": "...",
      "mid_prompt": "...",
      "production_prompt": "...",
      "eval_signals": ["..."]
    }}
  ],
  "track4_resume_drill": [
    {{
      "id": "rd1",
      "requisite_skill": "Python",
      "unproven_claim": "...",
      "drill_question": "...",
      "follow_up": "...",
      "proof_expected": "specific numbers, dates, decisions"
    }}
  ],
  "time_budget": {{"track1_pct":35,"track2_pct":25,"track3_pct":25,"track4_pct":15}},
  "opening_question": "Tell me about the project on your resume you're most proud of — and most embarrassed by."
}}
"""
    raw = await chat(
        messages=[{"role":"system","content":SYSTEM},{"role":"user","content":msg}],
        model="smart", temperature=0.4, max_tokens=4096, json_mode=True
    )
    return json.loads(raw)