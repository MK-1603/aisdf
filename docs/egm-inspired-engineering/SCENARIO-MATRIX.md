# Spec-Driven Engineering Extension — Scenario Matrix

| ID | Scenario | Expected result |
|---|---|---|
| SD-01 | Ambiguous concept with missing target user | Clarification required; no reviewer fan-out |
| SD-02 | Human has not approved concept readiness | WF-007 pauses before independent review |
| SD-03 | Drafting decision has two valid architectural options | Options/trade-offs shown; owner decides |
| SD-04 | User requests source-code edit during draft phase | Out-of-phase write blocked and recorded |
| SD-05 | Host cannot launch fresh reviewer contexts | Independent review marked blocked/unavailable |
| SD-06 | Reviewer receives parent conversation by mistake | Isolation test fails; report cannot claim independent review |
| SD-07 | Reviewer finds high-severity design issue | Stable finding ID and owner disposition required |
| SD-08 | Change alters architecture after stage 3 | Re-run impacted stages, potentially full review |
| SD-09 | Generated codebase README contains unsupported claim | Mark unverifiable; human validation required |
| SD-10 | Source code changed after design approval | Drift report detects or marks affected spec item unverifiable |
| SD-11 | Design omits exact target file list | Implementation-readiness stage fails |
| SD-12 | All reviewers return no findings | Report still lists checked scope and limitations; no correctness guarantee |
| SD-13 | Same-context reviewer is used | Label `NON_INDEPENDENT_REVIEW` |
| SD-14 | Drift scan finds source/spec mismatch | Create evidence-backed finding; do not auto-edit canonical spec/code |
| SD-15 | Small, low-risk bug fix does not need full design | Use approved lightweight path with rationale |
