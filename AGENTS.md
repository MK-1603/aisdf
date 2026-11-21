# AISDF Repository Agent Instructions

## Source of truth
- Read `README.md` for the human-facing overview.
- Read `PROJECT.md` for AISDF's purpose, scope, capabilities, and maturity.
- Read `00-GOVERNANCE/AISDF-RULEBOOK.md` and relevant domain/workflow standards before changing framework behavior.
- For target projects, treat their `PROJECT.md` as product truth and their `AGENTS.md` as the operating contract.

## Engineering rules
- Keep the core provider-neutral; isolate host-specific behavior in `adapters/`.
- Preserve user intent, scope lock, Change Only Law, least privilege, and human approval gates.
- Never overwrite existing project instructions or user-authored project documents without inspection and a proposed diff.
- Do not modify target application source during AISDF assessment/planning tooling.
- Keep generated artifacts traceable to requirement, finding, plan, and approval IDs.
- Never claim an agent, host integration, test, security scan, deployment, or review ran unless evidence exists.

## Validation
Run:
```bash
python tools/validate_repository.py
python -m pytest -q
python tools/aisdf_runtime/aisdf.py --help
python tools/aisdf_runtime/project.py --help
```

Update documentation, tests, changelog, and implementation status for behavior changes. Human maintainers retain release and licensing decisions.
