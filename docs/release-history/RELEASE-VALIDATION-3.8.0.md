# AISDF 3.8.0 — Release Validation Record

## Scope

This release consolidates the prior AISDF framework snapshot into a conventional repository-root layout, adds the root-level project README, promotes WF-007–WF-012 assets and runtime into first-class locations, and groups provider adapters under `adapters/`.

## Checks executed

| Check | Result | Evidence |
|---|---|---|
| Repository validator | PASS | `python tools/validate_repository.py` |
| Python test suite | PASS | `python -m pytest -q` — 8 passed |
| Runtime CLI entry point | PASS | `python tools/aisdf_runtime/aisdf.py --help` |
| Runtime end-to-end lifecycle | PASS | `tests/test_workflow_runtime_e2e.py` exercises WF-007–WF-012 artifact lifecycle and Git drift scope |
| Markdown relative links | PASS | Local relative-link scan; zero broken targets |
| Antigravity plugin manifest | PASS | JSON parsed successfully |
| ZIP integrity | See package build record | Archive integrity checked after packaging |

## Not certified by these checks

- Claude Code, Codex, Cursor, and Antigravity live host installation or version compatibility.
- Real model invocation, agent spawning, or genuine isolated reviewer context.
- Security-tool execution, deployment, production behavior, or application-level correctness.
- Legal licensing status. The license decision remains pending.

## Capability truth

The portable runtime creates and validates workflow artifacts. It does not call model APIs, edit target application source files, grant approvals, or independently prove semantic conformance. Human review and host-specific verification remain required.
