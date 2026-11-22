# AISDF 1.0 Quick Start

Requirements: Python 3.10+. No third-party runtime dependency.

1. Validate the repo: `python tools/validate_repository.py` and `python -m unittest discover -s tests -v`.
2. **In a real terminal** (approvals need a human at a keyboard), create a project and register yourself as approver:
   `python aisdf.py init --project ../demo --name "Demo" --owner "Your Name"`
3. Plan: `python aisdf.py plan --project ../demo --tasks examples/tasks.example.json`
4. Approve a task: `python aisdf.py approve --project ../demo --task-id DISC-001 --approver "Your Name"`
5. Make it ready (re-checks approval + dependencies): `python aisdf.py transition --project ../demo --task-id DISC-001 --to READY`
6. Record the work: either `python aisdf.py complete --project ../demo --task-id DISC-001 --actor "Your Name" --result SUCCEEDED --evidence report.md` (human did it) or, for `execute` tasks, `python aisdf.py run --project ../demo --task-id ID` after adding the program to `allowed_executables` in `../demo/.aisdf/policy.json`.
7. Check state and integrity: `python aisdf.py status --project ../demo` and `python aisdf.py verify-ledger --project ../demo`.
8. Before release: record checks, build the reviewer package, add findings, then `python aisdf.py gate --project ../demo`.

CI/automation: add `--non-interactive` to human commands. It is recorded as weaker assurance and the default release gate refuses it for sensitive actions.

Full command reference: `runtime/README.md`. What is enforced and what is not: `docs/framework/RULES-AND-ENFORCEMENT.md`. Using AISDF from a particular AI tool: `adapters/COMPATIBILITY.md`.
