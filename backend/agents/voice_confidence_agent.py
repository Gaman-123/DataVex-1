import json
from core.groq_client import chat
from models.types import VoiceOutput, Track

SYSTEM = """You are VoiceConfidenceAgent. Analyze HOW the candidate communicates.
Detect rehearsed delivery, genuine hesitation, over-polished stories.
Return ONLY valid JSON."""

TRACK_NOTES = {
    Track.conceptual:   "Hesitation on key tech terms, rising intonation = uncertainty",
    Track.lc:           "Silence at edge cases, narration quality while coding",
    Track.realworld:    "Over-polished = rehearsed. Raw stumbling = genuine experience",
    Track.resume_drill: "Hesitation on details they claimed to know well",
}

async def run_voice_confidence(
    track: Track,
    question_text: str,
    answer_transcript: str,
    audio_features: dict,
) -> VoiceOutput:

    msg = f"""
TRACK: {track.value}
WATCH FOR: {TRACK_NOTES[track]}

QUESTION: {question_text}
TRANSCRIPT: {answer_transcript}

AUDIO FEATURES:
- pace_wpm: {audio_features.get('pace_wpm','N/A')}
- energy_trajectory: {audio_features.get('energy_trajectory','N/A')}
- pause_count: {audio_features.get('pause_count','N/A')}
- max_pause_sec: {audio_features.get('max_pause_sec','N/A')}
- filler_count: {audio_features.get('filler_count','N/A')}
- pitch_variance: {audio_features.get('pitch_variance','N/A')}

Return JSON:
{{
  "confidence_level": 0.0-10.0,
  "hesitation_map": {{"term or moment": "what happened"}},
  "misalignment_flag": true|false,
  "misalignment_type": "rehearsed|bluffing|memorized_pattern|observed_not_done|null",
  "lc_narration_quality": "silent|some|full|null",
  "rw_polish_detected": true|false,
  "reasoning": "1-2 sentences"
}}
"""
    raw = await chat(
        messages=[{"role":"system","content":SYSTEM},{"role":"user","content":msg}],
        model="fast", temperature=0.2, json_mode=True
    )
    return VoiceOutput(**json.loads(raw))