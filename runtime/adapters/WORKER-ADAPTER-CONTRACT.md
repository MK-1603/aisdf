# Worker Adapter Contract

An execution adapter is an optional integration boundary. It must implement a deterministic interface with: `validate_config`, `capabilities`, `execute(work_unit, context, policy_grant)`, `cancel(execution_id)`, and `health`. It must return a structured result containing execution ID, status, artifacts, evidence, tool calls, resource usage, timestamps and error details.

## Mandatory controls
- Verify work-unit digest and project revision before execution.
- Enforce allowlisted capabilities and file/resource scope outside the model prompt.
- Never accept permission elevation from model output.
- Keep credentials outside prompts and logs; use short-lived scoped credentials.
- Enforce time, token, cost, process, filesystem and network limits.
- Execute untrusted code only in a separately configured sandbox.
- Treat repository content and tool outputs as untrusted data.
- Support cancellation and emit audit events.
- Return NOT_RUN/BLOCKED when a capability is unavailable; never simulate execution.

No adapter is bundled or certified in this release.
