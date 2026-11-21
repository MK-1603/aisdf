# AISDF Antigravity Plugin

A native Google Antigravity plugin bundle for AISDF's WF-007–WF-012 workflow protocol. Includes a task skill, always-on governance rules, and three specialized reviewer agent definitions.

## Install
- CLI: `agy plugin install <GitHub-repository-or-local-plugin-path>` (for a local directory, use the path supported by your installed CLI).
- App: Customizations → Marketplace/Installed → install from the supported local/GitHub plugin source.
- Validate locally with `agy plugin validate` from the plugin directory when the CLI is installed.

The portable runtime is distributed separately in `runtime/tools/aisdf.py`; copy it into the target project as `.aisdf-tools/aisdf.py`, then run `python .aisdf-tools/aisdf.py init --project .`.

## Reviewer isolation
The plugin defines reviewer roles, not a guarantee of independent execution. Use Antigravity subagents with isolated Git worktrees/sessions where available. Capture session and worktree evidence. If isolation is not demonstrable, record `NON_INDEPENDENT` or `BLOCKED`.

## Scope
No model API calls, deployment, source edits, or automatic approvals are performed by the plugin itself. Human approval remains mandatory.
