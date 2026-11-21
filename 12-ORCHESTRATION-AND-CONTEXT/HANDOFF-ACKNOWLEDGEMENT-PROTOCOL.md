# Handoff Acknowledgement Protocol

Sender packages a complete handoff envelope; receiver acknowledges receipt, confirms scope/permissions, validates referenced artifacts and explicitly accepts, rejects or requests clarification. Ownership transfers only after acceptance. Delegation cannot expand permissions. Record sender, receiver, timestamp, task state, evidence, outstanding risks and next action. Unacknowledged handoffs remain with the sender or designated coordinator.

## Additional detail (carried from the starter seed)
A handoff transfers responsibility and sufficient context, not just a conversational summary.

Required envelope: handoff ID/type, project/task IDs, sender/receiver, timestamp, schema/framework version, status and acknowledgement requirement.

Required payload: objective/scope, baseline/revision, source artifacts, requirements/decisions, assumptions/unknowns, dependencies, permissions, approvals, completed/incomplete work, changed files/branch/commits, commands/tests/evidence, risks, exact next action and escalation route.

Receiver must confirm access, baseline, scope, dependencies, approvals and permissions; then accept, reject or request clarification. Do not start material work before acceptance unless safe preparatory inspection is explicitly allowed. A handoff does not grant new authority.
