# Implementation Status - 1.0.0

Status words: SPECIFIED (documents only) - IMPLEMENTED (code exists) - TESTED (automated tests in `tests/`) - NOT INCLUDED.

| Capability | Status | Evidence |
|---|---|---|
| 31 engineering domains, 56 engines, WF-001-WF-013 | SPECIFIED | `00-...` to `30-...`, `engines/`, `workflows/` |
| 72 role contracts with per-role permission profiles | IMPLEMENTED + TESTED (manifests, docs sync, read-only reviewers) | `workforce/`, `tests/test_runtime_hardening.py` |
| Task DAG, state machine, budgets | IMPLEMENTED + TESTED | `tests/test_workforce_runtime.py` |
| Human approver allow-list, assurance level, digest-bound approval, revocation | IMPLEMENTED + TESTED | `ApprovalTests`, `ReadinessTests` |
| Dependency gating and no-fake-success | IMPLEMENTED + TESTED | `ReadinessTests` |
| Hash-chained audit ledger, tamper detection, v4 DB migration | IMPLEMENTED + TESTED | `verify-ledger`, `RegistryAndReleaseTests` |
| Governed local command executor (allow-list, scrubbed env, timeout, redaction, evidence) | IMPLEMENTED + TESTED (POSIX; process limits only) | `ExecutionTests` |
| Findings validation and human-only disposition | IMPLEMENTED + TESTED | `GateAndFindingTests` |
| Release gate | IMPLEMENTED + TESTED | `GateAndFindingTests` |
| Independent-review package | IMPLEMENTED + TESTED (independence itself UNVERIFIED by the runtime) | `ReviewAndMemoryTests` |
| Memory vault template + checker | IMPLEMENTED + TESTED | `memory/`, `ReviewAndMemoryTests` |
| Security tool lock (12 tools + 2 CI actions pinned by SHA) | IMPLEMENTED (pins resolved 2026-11-22) | `security/scanners.lock.json` |
| Security scanner execution | NOT INCLUDED (wire tools through `check run` / `check record`) | `security/README.md` |
| Model/provider adapters | CONTRACT ONLY - none bundled, none tested | `runtime/adapters/`, `adapters/COMPATIBILITY.md` |
| OS sandbox | NOT INCLUDED | use a container/VM |
| Autonomous AI workers | NOT INCLUDED | require a configured adapter |
| Multi-tool conformance (Claude Code, Cursor, Antigravity, Kimi, Qwen...) | NOT YET TESTED | `adapters/CONFORMANCE.md` |

A role prompt or manifest does not establish autonomous capability. See `docs/framework/MATURITY-MODEL.md` and `docs/framework/RULES-AND-ENFORCEMENT.md`.
