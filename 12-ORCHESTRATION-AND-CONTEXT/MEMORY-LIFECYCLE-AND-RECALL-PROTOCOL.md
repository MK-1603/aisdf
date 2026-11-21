# Memory Lifecycle and Recall Protocol

## Before a task
1. Resolve active user, organization, project and workspace scope.
2. Read canonical project state and current work-unit contract.
3. Retrieve only relevant, authorized memory.
4. Check provenance, status, freshness and confidence.
5. Build a bounded context pack with source references and omitted-material note.
6. Flag conflicts/stale records; do not silently choose one.

## During a task
Capture only durable outcomes: approved decisions and rationale, verified facts/constraints, evidence-backed lessons, task checkpoint/blocker/next action, and corrections. Do not save every chat message or turn speculation into fact.

## At completion/handoff
1. Update canonical work-unit/project state first.
2. Create a session summary: objective, outcome, changed files, actual commands/tests, evidence, risks and next action.
3. Link artifacts rather than duplicating large documents.
4. Propose durable memories separately from transient notes.
5. Apply consent, sensitivity and approval rules.
6. Persist through an authorized adapter, verify by reading back, report exact records changed.

## Reconciliation
When new evidence conflicts with memory, preserve both sources, mark the older claim DISPUTED or SUPERSEDED, identify affected decisions, and seek authorized resolution if project direction changes. Never rewrite history to hide conflict.

## Recall response
Expose answer/abstention, memory IDs and source paths, status and verified date, confidence/limitations, and whether content is fact, approved decision, assumption or recommendation.

## Failure states
`NOT_FOUND`, `LOW_CONFIDENCE`, `STALE`, `CONFLICTED`, `ACCESS_DENIED`, `STORE_UNAVAILABLE`, `WRITE_NOT_VERIFIED`.

Failure to recall is not proof that information never existed.
