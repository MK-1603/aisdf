# Pause, Resume and Checkpoint Protocol

Before pausing, record project/task IDs, baseline revision, current branch/commit, completed work, uncommitted changes, commands/tests and results, open issues, assumptions, risks, approvals, next action and stop conditions. On resume, reload the checkpoint, verify repository state has not drifted, re-check permissions and freshness-sensitive facts, then continue only after reconciling differences. Never assume prior session context is authoritative.

## Additional detail (carried from the starter seed)
Pause when a required decision/approval/access/dependency is missing, a safety issue appears, the environment/budget limit is reached or continued execution is unsafe.

A checkpoint records:
- Project, workflow and task IDs.
- Baseline revision and current branch.
- Completed and incomplete steps.
- Files/artifacts created or changed.
- Commands/actions actually performed.
- Test results and logs.
- Current state and blocker.
- Uncommitted/unpushed changes.
- Required input/approval to resume.
- Exact next action and stop conditions.

On resume, revalidate the baseline and permissions, then continue from the first incomplete step. Do not assume a timed-out action failed; inspect actual state before retrying.
