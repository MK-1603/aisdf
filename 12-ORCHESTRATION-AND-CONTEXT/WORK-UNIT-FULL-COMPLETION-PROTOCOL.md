# Work-Unit Full Completion Protocol

A work unit is complete only when its objective and acceptance criteria are met; required outputs exist; allowed changes are recorded; applicable tests/reviews are run; evidence is attached; risks and deviations are reported; project state is updated; and a handoff/completion report is produced. Mark individual criteria PASS, FAIL, NOT_RUN, BLOCKED, NOT_APPLICABLE or WAIVED. WAIVED requires an authorized waiver. “Code written” is not equivalent to “work complete.”

## Additional detail (carried from the starter seed)
Before starting, define ID, objective, scope, inputs, baseline, dependencies, outputs, acceptance criteria, verification, permissions, approvals, budget and stop conditions.

## Completion sequence
1. Read applicable instructions and rules.
2. Confirm inputs, access, baseline and approvals.
3. Execute all required activities.
4. Create every required output.
5. Validate output structure and completeness.
6. Run required checks.
7. Record evidence and unresolved issues.
8. Update project state and traceability.
9. Prepare handoff.
10. Obtain acknowledgement where required.
11. Mark `DONE` only when all mandatory exit criteria pass.

States: `NOT_STARTED`, `IN_PROGRESS`, `BLOCKED`, `NEEDS_APPROVAL`, `FAILED`, `PARTIALLY_COMPLETED`, `READY_FOR_REVIEW`, `VERIFIED`, `DONE`, `CANCELLED`, `WAIVED`.

Partial work is not success. A waiver requires authorized owner, reason, impact and review/expiry condition.
