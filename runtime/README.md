# AISDF Runtime (1.0)

A deterministic, local control plane using only Python's standard library and SQLite. Run it with `python aisdf.py <command>` from the repository root (same as `python runtime/aisdf_runtime/workforce.py`).

## Commands
| Command | Purpose |
|---|---|
| `init --project P --name N [--owner NAME]` | Create PROJECT.md, AGENTS.md, `.aisdf/` with deny-all `policy.json`; register first approver |
| `approvers add\|list` | Manage the human approver allow-list |
| `workers` | List the 72 role manifests |
| `plan --project P --tasks FILE` | Validate and store tasks (workers, actions, budgets, cycles, argv commands). Changed tasks lose approval |
| `approve --task-id ID --approver NAME` | Registered human approval, bound to the task digest |
| `transition --task-id ID --to READY\|BLOCKED\|CANCELLED` | READY re-verifies approval, digest and dependencies |
| `run --task-id ID` | Execute an approved `execute` task as an allow-listed local command, with evidence |
| `complete --task-id ID --actor NAME --result R [--evidence F]` | Record human-performed work (evidence required for success) |
| `check run\|record\|list` | Record release-gate checks (runtime-executed, or external with evidence) |
| `findings add\|resolve\|list` | Schema-validated EGM findings; human disposition only |
| `review-package --out DIR` | Build hashed input for an independent reviewer (no memory/chat) |
| `gate [--policy FILE]` | Evaluate the release gate; exit 2 if BLOCKED |
| `verify-ledger` | Check the hash chain and task integrity; exit 2 on tampering |
| `status` | Show tasks and waiting dependencies |
| `memory-check --vault DIR` | Validate memory notes' provenance and flag injected instructions |

## Files created in a project
`.aisdf/policy.json` (approvers, allowed_executables, env_allowlist) - `.aisdf/workforce.sqlite3` (tasks + hash-chained events) - `.aisdf/evidence/` - `.aisdf/checks/` - `.aisdf/findings/` - `.aisdf/gate-report.json`.

## Exit codes
0 OK - 1 error/refused - 2 gate BLOCKED or ledger tampering - 3 executed command failed.

## What it does not do
It does not call an LLM, provide a sandbox (process limits only; no network or filesystem isolation), run security scanners by itself, or deploy. Model/tool adapters implement `runtime/adapters/WORKER-ADAPTER-CONTRACT.md`. The ledger is tamper-evident, not tamper-proof: protect `.aisdf/policy.json` with OS permissions and CODEOWNERS. See `docs/framework/RULES-AND-ENFORCEMENT.md`.

## Upgrading from 4.0.0 databases
Existing `.aisdf/workforce.sqlite3` files are migrated automatically (new columns). Old events are counted as "legacy unchained"; old tasks have no stored content, so re-run `plan` before approving them.
