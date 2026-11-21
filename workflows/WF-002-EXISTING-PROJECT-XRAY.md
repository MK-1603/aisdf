# WF-002 — Existing Project X-Ray

Follow the required sequence: Inspect → Understand → Analyze → Discover → Compare → Document → Approve → Implement → Verify.

1. Establish repository baseline and available execution environment.
2. Inspect manifests, source tree, documentation, tests, CI, secrets handling and deployment configuration (never expose secret values).
3. Map current features, architecture, data/API boundaries and dependencies.
4. Run only authorized, non-destructive checks; record commands and actual results.
5. Identify issues and rank by impact, likelihood, evidence and effort.
6. Compare improvement options and record trade-offs.
7. Produce a change proposal with files likely affected, migration, rollback and tests.
8. Obtain approval for material changes.
9. Implement minimal changes with branch/commit discipline.
10. Run regression/security/quality checks and issue completion report.

Do not claim a full audit if parts of the repository, runtime or infrastructure were inaccessible.
