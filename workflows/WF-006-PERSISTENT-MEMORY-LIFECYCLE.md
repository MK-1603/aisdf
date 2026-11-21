# WF-006 — Persistent Memory Lifecycle

**Status: PROPOSED.** Requires approved governance and a conformant adapter.

## Trigger
Task completion, approved decision, verified reusable lesson, or a new session requiring project context.

## Phases
1. Resolve project/workspace/user scope and access.
2. Capture candidate decisions, facts, lessons, checkpoints and next actions.
3. Classify durable/transient, project/user/reusable and sensitivity.
4. Validate sources, duplicates, freshness, conflicts and confidence.
5. Obtain approval for preferences, sensitive categories, consequential decisions and policy-defined writes.
6. Persist through an authorized adapter; preserve revision history.
7. Re-read exact records and verify content/revision.
8. Update rebuildable indexes; indexing failure does not negate a verified canonical write.
9. Recall only relevant, authorized and bounded records in later sessions.
10. Reconcile stale/conflicting records and link replacements.
11. Report stored, skipped, rejected and unresolved candidates.

## Exit criteria
- Required metadata and provenance exist.
- No prohibited secret or unapproved sensitive data was stored.
- Writes are verified or explicitly reported unverified.
- Canonical project state remains authoritative.
- Conflicts, stale records and next actions are visible.

## Outcomes
`MEMORY_UPDATED`, `NO_DURABLE_MEMORY`, `APPROVAL_REQUIRED`, `BLOCKED`, `WRITE_FAILED`, `WRITE_UNVERIFIED`, `CONFLICT_REQUIRES_REVIEW`.

Read-only recall is default. This workflow does not imply scheduled agents, hooks, network access or background processing.
