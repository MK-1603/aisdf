# AISDF Design Specification Standard

## Required document header

- Stable design ID and title.
- Status: `CONCEPT`, `DRAFT`, `IN_REVIEW`, `CHANGES_REQUESTED`, `APPROVED`, `IMPLEMENTING`, `IMPLEMENTED`, `VERIFIED`, `SUPERSEDED` or `REJECTED`.
- Author, owner, reviewers, creation/update dates and source revision.
- Related project baseline, requirements, decisions and risk records.

## Required sections

1. Executive summary and decision requested.
2. Problem statement, evidence and affected users/systems.
3. Goals, measurable outcomes and explicit non-goals.
4. Current-state/codebase findings with paths and revisions.
5. Proposed behavior and user/system workflows.
6. Functional and non-functional requirements.
7. Architecture, components, boundaries and data/control flow.
8. API/event/data contracts and schema evolution.
9. Alternatives considered, including reuse/YAGNI and why rejected.
10. Security, privacy, threat model and trust boundaries.
11. Reliability, failure modes, retries, idempotency and recovery.
12. Performance, capacity, cost and operational considerations.
13. Observability, metrics, logs, traces and alerting.
14. Migration, compatibility, rollout and rollback.
15. Implementation plan with exact repository-relative file allowlist.
16. Test plan with acceptance criteria and independent verification.
17. Risks, assumptions, unknowns and open questions.
18. Decision log, approvals and change history.

## Semantic boundaries

Separate **feature-level design** (problem, behavior, boundaries, architecture and invariants) from **implementation-level plan** (specific files, functions, schemas, migrations, commands and tests). Do not let implementation detail obscure the architectural decision; do not let high-level prose substitute for actionable implementation instructions.

## Drafting rules

- Draft one section at a time and persist it as a file.
- Obtain approval or revision feedback at each material section gate.
- For material decisions with multiple defensible options, present mechanisms, trade-offs and failure conditions; the human owner chooses.
- Do not fabricate repository facts. Cite paths, symbols, revisions and command/test evidence.
- Keep assumptions, facts, recommendations and unresolved questions distinct.
- No production source-code changes during concept, drafting or review phases.
- The final implementation allowlist must name exact files to create/modify/delete. A glob requires explicit justification and a bounded generated-output rule.
