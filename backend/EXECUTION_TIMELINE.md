# Agent Execution Timeline

This documents the interview agent execution order and parallelism.

## On candidate upload (once)

Agent 1 — ResumeAgent
- Runs alone, sequentially. Takes resume + requirements, returns analysis.
- Done before anything else happens.

## On session create (once)

Agent 2 — QuestionArchitectAgent
- Runs alone, sequentially. Reads resume analysis, builds the full question plan.
- Done before interview starts.

## On every answer submission (the hot loop)

Agent 3 — EvaluatorAgent   ──┐
                              ├── `asyncio.gather()` → run in PARALLEL
Agent 4 — VoiceConfidenceAgent┘

↓ both finish

Agent 5 — DepthProberAgent
- Runs ONLY IF evaluator decides `follow_up` or `stress_test`. Otherwise skipped.

↓

Agent 6 — OrchestratorAgent
- Always runs. Takes outputs from Agents 3,4,5 and decides next action.

## On session close (once)

Agent 7 — SessionAnalystAgent
- Runs alone. Reads ALL rounds at once and produces the final report.

## Notes
- In `routers/sessions.py` agents 3 & 4 are started concurrently via `asyncio.create_task()` and awaited together with `asyncio.gather()` to reduce round latency.
- The orchestrator runs only after evaluator, voice confidence and optional depth prober complete.
- Logging has been added to `routers/sessions.py` to record start/finish times and decisions for easier observability and testing.
