# AISDF Runtime

The v4.0 runtime is a deterministic, local control-plane reference implementation using Python's standard library and SQLite.

## Commands

```bash
python runtime/aisdf_runtime/workforce.py workers
python runtime/aisdf_runtime/workforce.py init --project ../sample --name "Sample Project"
python runtime/aisdf_runtime/workforce.py plan --project ../sample --tasks examples/tasks.example.json
python runtime/aisdf_runtime/workforce.py approve --project ../sample --task-id DISC-001 --approver "Project Owner"
python runtime/aisdf_runtime/workforce.py status --project ../sample
```

`plan` validates worker IDs, requested action categories, dependency existence/cycles, budgets and sensitive-action approval requirements. It stores planned tasks and audit events in `.aisdf/workforce.sqlite3`. `approve` records human approval against the task's immutable digest. `transition` enforces the documented state machine. Direct transition to RUNNING is intentionally disabled until a configured execution adapter exists.

## What it does not do

It does not invoke an LLM, execute arbitrary code, launch remote agents, provide a sandbox, or deploy software. Model/tool adapters must implement `runtime/adapters/WORKER-ADAPTER-CONTRACT.md`, be separately configured and tested, and run behind an enforceable sandbox and permission boundary.
