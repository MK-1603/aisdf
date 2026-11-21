# E-024 — Stack Selection

## Purpose
Compare stack choices against requirements and team capability.

## Scope
Perform the capability described above within the approved project baseline and task boundary. Produce explicit, reviewable artifacts and evidence.

## Non-goals
- This engine is a capability specification, not a standalone executable or autonomous service.
- It does not grant permissions, approve its own decisions or bypass project governance.
- It must not fabricate facts, execution results, compatibility or evidence.

## Trigger
Invoke when a workflow reaches this capability and the required inputs are available.

## Required inputs
- Project profile and current project state.
- Relevant source documents, repository artifacts and approved decisions.
- Task/work-unit contract, scope, permissions and acceptance criteria.
- Applicable governance rules and evidence requirements.

## Outputs
- A structured result documenting findings, decisions, assumptions, unknowns and limitations.
- Updated project artifacts/records required by the workflow.
- Evidence references and a handoff or completion report.

## Procedure
1. Read the project baseline, applicable rules and task contract.
2. Confirm scope, authority, inputs and dependencies; stop if a blocker prevents safe work.
3. Inspect the supplied evidence and identify provenance and freshness.
4. Perform the capability using the smallest sufficient method.
5. Separate facts, approved decisions, assumptions, inferences and unknowns.
6. Evaluate alternatives and risks when the decision is material.
7. Produce outputs in the specified format and link supporting evidence.
8. Check acceptance criteria; record PASS/FAIL/NOT_RUN/BLOCKED/NOT_APPLICABLE/WAIVED.
9. Update project state and prepare a handoff to the next owner.

## Decision rules
- Prefer authoritative, current, primary sources for changing technical claims.
- Do not infer missing project facts; ask only blocking questions.
- Apply least privilege, Change Only Law and No AI Slope.
- Escalate conflicts, irreversible actions, scope changes and unapproved costs.

## Dependencies
Project profile, applicable governance, source evidence, and upstream workflow outputs. Specific dependencies must be listed in the work unit.

## Responsible role
Assigned project role/owner. The workflow coordinator may route work but cannot expand the assignee's permissions.

## Tool capabilities and permissions
Use only capabilities verified for the exact tool/version/plan/environment. Default to read-only. Any write, external communication, purchase, push, merge or deployment requires explicit task authorization.

## Freshness and alternatives
Re-verify version-sensitive information at the time of decision. Compare viable alternatives for material choices; document when no alternative is viable.

## Failure behavior
Return BLOCKED or FAILED with the cause, attempted actions, evidence, impact and recovery recommendation. Do not silently skip required checks.

## Evidence
Source references, inspected file paths/revisions, commands and outputs actually executed, test results, review records and approval IDs as applicable.

## Acceptance criteria
- Output addresses the engine responsibility and requested scope.
- Findings are traceable to source evidence or clearly marked as assumptions.
- Risks, unknowns and limitations are visible.
- Required approvals and validation states are recorded.

## Exit criteria
All required outputs exist, acceptance statuses are recorded, project state is updated and the next handoff is prepared.


## Engine-specific execution contract

### Responsibility
Select a technology stack based on requirements, team capability and lifecycle cost.

### Minimum input contract
Technology evidence, constraints, alternatives.

### Required output contract
Stack decision record, tradeoffs, compatibility risks.

### Decision and safety conditions
- Confirm that the input evidence is sufficient for this specific responsibility.
- Record source, revision/date and confidence for material findings.
- Separate observed facts, user-approved decisions, assumptions and recommendations.
- Do not select based only on popularity or novelty.

### Engine-specific acceptance tests
- Chosen versions and support status are recorded.
- A reviewer can reproduce the result from the recorded inputs and evidence.
- Missing inputs or unavailable tools produce an explicit BLOCKED/NOT_RUN state, not a guessed result.

### Minimum test scenarios
1. **Valid input:** complete required inputs; produce all required outputs.
2. **Missing input:** omit a critical input; identify the blocker and stop dependent work.
3. **Conflicting evidence:** surface the conflict and preserve both source references.
4. **Out-of-scope request:** refuse or escalate the request without expanding permissions.
5. **Recovery:** resume from a checkpoint and verify the project baseline before continuing.
