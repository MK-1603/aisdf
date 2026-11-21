# AISDF v4.0 Quick Start

1. Install Python 3.10 or newer.
2. Extract the repository and open its root.
3. Run `python tools/validate_repository.py`.
4. Run `python -m unittest discover -s tests -v`.
5. List workers: `python runtime/aisdf_runtime/workforce.py workers`.
6. Initialize a project: `python runtime/aisdf_runtime/workforce.py init --project ../demo --name "Demo"`.
7. Copy `examples/tasks.example.json` into the target project's `.aisdf/` folder or pass it directly to the planner.
8. Plan tasks: `python runtime/aisdf_runtime/workforce.py plan --project ../demo --tasks examples/tasks.example.json`.
9. Approve tasks by ID: `python runtime/aisdf_runtime/workforce.py approve --project ../demo --task-id DISC-001 --approver "Your Name"`.
10. Inspect state: `python runtime/aisdf_runtime/workforce.py status --project ../demo`.

Planning and approval do not execute work. Use a human operator or a separately configured and secured adapter. See `runtime/adapters/WORKER-ADAPTER-CONTRACT.md`.
