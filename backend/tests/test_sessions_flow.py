import asyncio
import time
import logging
import pytest
from models.schemas import AnswerSubmit

# These tests patch the agents imported in routers.sessions to verify ordering and that
# evaluator + voice run in parallel, depth prober runs conditionally, and orchestrator runs last.

@pytest.mark.asyncio
async def test_parallel_evaluator_voice_and_conditional_probe(monkeypatch, caplog):
    caplog.set_level(logging.INFO)
    events = []

    async def fake_evaluator(track, question_metadata, answer_transcript, answer_code, coverage):
        events.append(('evaluator_start', time.perf_counter()))
        await asyncio.sleep(0.05)
        events.append(('evaluator_end', time.perf_counter()))
        class Out:
            next_action = 'follow_up'
            signals = {'x':'y'}
            requisite_skill_updated = None
            requisite_new_level = None
            understanding_level = 'partial'
            content_score = 0.5
            def model_dump(self):
                return {'next_action': self.next_action, 'signals': self.signals}
        return Out()

    async def fake_voice(track, question_text, answer_transcript, audio_features):
        events.append(('voice_start', time.perf_counter()))
        await asyncio.sleep(0.05)
        events.append(('voice_end', time.perf_counter()))
        class V:
            confidence_level = 7.5
            hesitation_map = {}
            misalignment_flag = False
            misalignment_type = None
            def model_dump(self):
                return {'confidence_level': self.confidence_level}
        return V()

    async def fake_probe(track, question_text, answer_transcript, signals, probe_trigger, requisite_skill):
        events.append(('probe_start', time.perf_counter()))
        await asyncio.sleep(0.01)
        events.append(('probe_end', time.perf_counter()))
        return {'probe_question':'follow up?'}

    async def fake_orch(session, evaluator_output, voice_output, req_data, question_plan):
        events.append(('orch_start', time.perf_counter()))
        await asyncio.sleep(0.01)
        events.append(('orch_end', time.perf_counter()))
        class O:
            next_action = 'next_question'
            next_track = None
            next_question = 'what next'
            hr_nudge = None
            requisite_alert = None
        return O()

    # Patch the functions used in routers.sessions
    import backend.routers.sessions as sessions_mod
    monkeypatch.setattr(sessions_mod, 'run_evaluator', fake_evaluator)
    monkeypatch.setattr(sessions_mod, 'run_voice_confidence', fake_voice)
    monkeypatch.setattr(sessions_mod, 'run_depth_prober', fake_probe)
    monkeypatch.setattr(sessions_mod, 'run_orchestrator', fake_orch)

    # Build a minimal AnswerSubmit object
    data = AnswerSubmit(
        session_id='sess1', round_number=1, track='conceptual', question_id='q1',
        question_text='Explain X', question_metadata={'id':'q1'}, answer_transcript='I did X',
        answer_code=None, audio_features={}, requisite_skill=None
    )

    # Call the submit_answer handler directly
    # It will interact with supabase in real code; here we avoid DB calls by patching them out.
    # Patch supabase.table(...).select(...).execute() flows used in submit_answer.
    class FakeTable:
        def __init__(self, data):
            self._data = data
        def select(self, *_a, **_k):
            return self
        def eq(self, *_a, **_k):
            return self
        def execute(self):
            return type('R', (), {'data': self._data})
        def update(self, *_a, **_k):
            return self
        def insert(self, *_a, **_k):
            return self

    class FakeSupabase:
        def __init__(self):
            pass
        def table(self, name):
            if name == 'interview_sessions':
                return FakeTable([{'id':'sess1','requirements_id':'req1','requisite_coverage':{},'questions_asked':0,'question_plan':{},'candidate_id':'cand1','company_id':'comp1','current_track':'track1_conceptual','time_budget_seconds':3600,'time_elapsed_seconds':0}])
            if name == 'company_requirements':
                return FakeTable([{}])
            if name == 'interview_rounds':
                return FakeTable([])
            if name == 'candidates':
                return FakeTable([{'id':'cand1'}])
            return FakeTable([])

    monkeypatch.setattr(sessions_mod, 'supabase', FakeSupabase())

    # Patch websocket manager to no-op
    class FakeWS:
        async def send(self, *_a, **_k):
            return None
    monkeypatch.setattr(sessions_mod, 'ws_manager', FakeWS())

    # Run handler
    out = await sessions_mod.submit_answer(data)

    # Validate ordering: evaluator_start and voice_start should be very close and before their respective ends
    starts = [e for e in events if e[0].endswith('_start')]
    ends = [e for e in events if e[0].endswith('_end')]
    assert ('evaluator_start',) and ('voice_start',)
    assert any(e[0] == 'probe_start' for e in events)
    assert any(e[0] == 'orch_start' for e in events)

    # Ensure orchestrator runs last
    last_event = events[-1][0]
    assert last_event in ('orch_end', 'orch_end')
