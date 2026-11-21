# 50 — Harness Engineering Verification Plan

**Status:** TEST PLAN DEFINED — execution is not implied.  
**Specification:** `../SPECIFICATIONS/50-harness-engineering.md`

## Preconditions
- Approved scope, architecture, threat model and acceptance criteria.
- Isolated test environment with synthetic/non-sensitive data.
- Exact software/model/tool/configuration versions recorded.
- Least-privilege test identities and cleanup/rollback procedure.

## Required test cases
1. Nominal valid path and expected outcome.
2. Boundary, malformed, duplicate and maximum-size inputs.
3. Missing, stale, contradictory and unauthorized inputs.
4. Dependency outage, timeout, partial completion and resource exhaustion.
5. Restart, retry, checkpoint/resume, rollback or restore.
6. Injection, privilege escalation, tenant isolation and secret exposure.
7. Parallel operations, conflicting updates, races and duplicate requests.
8. Representative, peak and worst-case performance and budget enforcement.
9. Logs, metrics, traces, audit events and actionable failure signals.
10. Version/configuration/schema change and backward compatibility.

## Topic-specific checks
- Verify tool schemas, argument validation, permission enforcement and side-effect classification.
- Prove sandbox restrictions are enforced by runtime/OS, not prompts alone.
- Test prompt injection through files, retrieval, memory, browser and tool outputs.
- Test context provenance/freshness, tenant isolation, redaction, model drift and kill switch.

## Evidence to retain
- Test ID, environment and exact versions.
- Synthetic fixture identifier, action/command, timestamp and result.
- Expected versus actual outcome and redacted logs/metrics/trace IDs.
- Defect severity, owner, reviewer and retest evidence.

## Exit criteria
- Required tests are PASS or explicitly `NOT_RUN`/`BLOCKED` with rationale and owner.
- Critical/high defects are visible and not hidden by summary status.
- Security and recovery tests meet the approved risk threshold.
- Independent review and residual-risk record exist for high-impact behavior.

A written test plan is not a test result. Promote maturity only after execution evidence is reviewed.
