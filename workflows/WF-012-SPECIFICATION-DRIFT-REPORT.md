# WF-012 — Specification-to-Code Drift Report

**Purpose:** Detect where approved design documents, architecture records and repository documentation diverge from the current implementation.

## Procedure
1. Resolve the approved design revision and current repository commit/branch.
2. Parse requirements, architecture decisions, interfaces, data contracts, file boundaries and implementation claims.
3. Inspect corresponding source paths, symbols, tests, schemas and deployment/configuration evidence.
4. Classify each item: `MATCH`, `IMPLEMENTATION_DRIFT`, `SPEC_DRIFT`, `MISSING_IMPLEMENTATION`, `UNVERIFIABLE`, `STALE_SOURCE`, `NOT_APPLICABLE`.
5. Attach exact paths, line/symbol references, revisions and confidence; do not infer runtime behavior from names alone.
6. Identify affected requirements, operational/security impact and likely owner.
7. Recommend one of: update code, update spec, record approved deviation, investigate, or retire obsolete spec.
8. Human owner approves any source/spec change. Changes follow normal change-control and test gates.
9. Preserve historical reports and compare deltas over time.

## Schedule and triggers
Run before major releases, after architecture-affecting changes, during maintenance review and optionally on a scheduled cadence. Scheduled execution must be opt-in, scoped and cost-bounded.

## Output
A versioned drift report with scope, source revisions, findings, evidence, severity, owner, disposition and follow-up status.
