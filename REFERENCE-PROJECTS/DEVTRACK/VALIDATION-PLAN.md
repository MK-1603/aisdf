# DevTrack Validation Plan

## Gate 0 — Intake
Input: this brief. Output: approved project profile, assumptions and non-goals. Pass: owner accepts scope and unresolved questions are recorded.

## Gate 1 — Requirements
Produce user stories, functional/non-functional requirements, IDs and acceptance criteria. Pass: every MVP requirement is testable and approved.

## Gate 2 — UX
Produce navigation, core flows, empty/loading/error states, responsive behavior and accessibility considerations. Pass: owner review completed; critical flows have acceptance criteria.

## Gate 3 — Architecture
Produce context/container view, data model, API boundaries, auth decision (including whether MVP can be single-user/local), security threat notes, deployment plan and ADRs. Pass: tradeoffs and risks approved.

## Gate 4 — Implementation
Break work into bounded work units. Each unit has owner, files, permissions, acceptance and tests. Pass: implementation diff is within approved scope.

## Gate 5 — Verification
Execute unit/integration/e2e tests appropriate to the stack; run dependency and secret checks; conduct manual accessibility and security review. Record PASS/FAIL/NOT_RUN/BLOCKED. Pass: no unresolved release-blocking defect.

## Gate 6 — Staging
Deploy only with explicit authorization. Record artifact/version, environment, deployment command/action, result, smoke tests and rollback method. Pass: critical user journeys work in staging.

## Gate 7 — Closeout
Publish traceability matrix, test evidence, residual risks, operational notes and completion report. Pass: independent reviewer can reproduce the evidence.

## AISDF evaluation metrics
Requirement traceability; acceptance-test pass rate; defect escape count; unauthorized scope changes; unverified claims; blocked-task recovery success; reproducibility; reviewer effort. Define measurement methods before scoring.
