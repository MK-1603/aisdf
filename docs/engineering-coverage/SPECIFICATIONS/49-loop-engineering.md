# 49 — Loop Engineering

**Engineering area:** Agent control loops and feedback systems  
**Maturity:** SPECIFIED — implementation and production verification are project-specific.

## Purpose
Engineering bounded, observable, recoverable feedback loops for software automation and AI-agent workflows.

## Core concepts and mechanisms
- Observe state; evaluate goals and constraints; plan; act; capture results; verify; select the next transition.
- Agent loop patterns: plan-act-observe, tool-use loops, evaluator-optimizer, reflection/revision and event-driven continuation.
- Termination: explicit success/failure predicates, iteration/time/token/cost/tool-call budgets, no-progress detection and human escalation.
- State machines, checkpoints, durable versus ephemeral state, idempotent resumption and audit history.
- Feedback quality, evaluator independence, noisy/delayed signals, metric gaming and reward hacking.
- Stability controls: bounded retries, backoff with jitter, hysteresis, cooldowns, rate limits and circuit breakers.
- Parent/child loops, shared budgets, concurrency limits, cancellation propagation and conflict arbitration.

## Required inputs
- Approved goal, measurable success criteria and non-goals.
- Authoritative state snapshot and source-of-truth references.
- Allowed actions, tools, permissions and prohibited actions.
- Budgets, deadlines, retry policy, risk tier and approval requirements.
- Evaluation method, evidence threshold and recovery checkpoint.

## Required outputs
- Loop state machine and transition table.
- Termination, pause, approval, cancellation and escalation policy.
- Budget/retry configuration and checkpoint/audit schema.
- Evaluation evidence, recovery runbook and residual-risk record.

## Security, reliability and failure modes
- Infinite/runaway loops, no-op repetition and oscillation.
- False-positive evaluators, self-grading bias and reward hacking.
- Duplicate side effects after retry/resume and concurrent state races.
- Budget exhaustion, tool amplification, stale state and unbounded context.
- Prompt injection or untrusted observations steering execution out of scope.

Treat external content, retrieved memory and tool outputs as untrusted until validated. Apply least privilege, data minimization, tenant isolation, safe failure behavior and explicit authorization.

## Implementation workflow
1. Define goal predicates and distinguish verified completion from plausible output.
2. Define states, transitions and invariants before execution.
3. Set enforceable iteration, time, token/compute, monetary and tool-call budgets.
4. Specify stop, pause, approval, cancellation, timeout, retry and recovery semantics.
5. Make side effects idempotent or protect them with deduplication/transaction boundaries.
6. Record observations, decisions, actions and results with provenance and redaction.
7. Use independent verification for high-impact outcomes.
8. Test noisy, delayed, contradictory and missing feedback; prove safe termination.
9. Release with monitoring, kill switch, owner and rollback/recovery plan.

## Verification strategy
Finite-state transition coverage; bounded termination and budget enforcement; no-progress/oscillation; retry/idempotency; cancellation/checkpoint-resume; evaluator false-positive/negative; prompt-injection/out-of-scope actions; concurrency and failure injection.

## Companion test plan
`../TEST-PLANS/49-loop-engineering-tests.md`

## Acceptance criteria
- Applicability is justified; unnecessary complexity is rejected.
- Architecture, alternatives, assumptions, security boundaries and operational ownership are documented.
- Failure, recovery and observability behavior are explicit.
- Tests have reproducible evidence; unrun checks are `NOT_RUN`.
- Production use has rollback/recovery, monitoring and accountable ownership.

## Related AISDF capabilities
Reuse existing engines, workflows, schemas and governance. Do not allocate duplicate engine IDs or imply that a documented capability is an implemented runtime. Record exact project dependencies in the work unit.

## Status vocabulary
`NOT_ASSESSED` · `SPECIFIED` · `DESIGNED` · `IMPLEMENTED` · `TESTED` · `INDEPENDENTLY_VERIFIED` · `PRODUCTION_VERIFIED` · `NOT_APPLICABLE` · `BLOCKED`.
