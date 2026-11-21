# Pause, Resume and Checkpoint Protocol

Before pausing, record project/task IDs, baseline revision, current branch/commit, completed work, uncommitted changes, commands/tests and results, open issues, assumptions, risks, approvals, next action and stop conditions. On resume, reload the checkpoint, verify repository state has not drifted, re-check permissions and freshness-sensitive facts, then continue only after reconciling differences. Never assume prior session context is authoritative.
