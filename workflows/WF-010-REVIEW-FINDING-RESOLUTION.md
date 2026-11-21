# WF-010 — Review Finding Triage and Resolution

## Procedure
1. Assign stable finding IDs and deduplicate only when root cause and evidence are materially equivalent.
2. Classify severity: `BLOCKER`, `CRITICAL`, `HIGH`, `MEDIUM`, `LOW`, `NOTE`.
3. Record exact document section/source evidence, impact, affected requirement and recommended action.
4. Human owner chooses `ACCEPT`, `REJECT_WITH_RATIONALE`, `DEFER`, `DUPLICATE_OF`, or `NEEDS_DISCUSSION`.
5. Accepted changes are applied to the design artifact; update decision log, requirements and traceability.
6. Re-run the affected review stage and any downstream stage invalidated by the change. Re-run full review if architecture, trust boundary, data model or major scope changes.
7. Close a finding only with evidence that the change resolves the stated concern. Rejected/deferred findings remain visible with rationale/owner/due condition.
8. Obtain human approval and submit the design through the project's normal review/version-control process.

## Rules
- AI cannot self-approve a material design decision or mark its own finding resolved without evidence.
- Do not delete dissenting or rejected findings from the audit trail.
- A severity downgrade requires rationale and human approval.
- No implementation until blockers are closed or explicitly accepted under governance policy.
