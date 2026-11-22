# AISDF 1.0 — Complete Step-by-Step Operating Guide

## Step 1 — Install and validate
Install Python 3.10+. Extract the repository. Run `python tools/validate_repository.py` and `python -m unittest discover -s tests -v`. Do not proceed if checks fail.

## Step 2 — Initialize the target project
Run `python aisdf.py init --project ../your-project --name "Your Project" --owner "Your Name"`. AISDF creates `PROJECT.md`, `AGENTS.md` and `.aisdf/` (with a deny-all `policy.json`) without overwriting existing project files, and registers you as the first approver. Type this in a real terminal.

## Step 3 — Inspect the existing repository
Run the existing project inventory helper: `python tools/aisdf_runtime/project.py assess --project ../your-project`. This is a deterministic file inventory, not semantic code understanding.

## Step 4 — Complete project truth
Use a human engineer or connected coding assistant to inspect source, tests, build configuration, APIs, migrations, dependencies and deployment. Complete `PROJECT.md` with evidence. Distinguish implemented, partially implemented, documented-only, planned, missing and unknown. Run `python tools/aisdf_runtime/project.py check --project ../your-project`.

## Step 5 — Select specialists
Open `workforce/ROLE-CATALOGUE.md`. Select only roles relevant to the project. Review each role contract and worker manifest. Confirm the role's maturity and available adapter before assigning execution.

## Step 6 — Define work units
Create a JSON array using `workforce/schemas/work-unit.schema.json`. Each task must have a unique ID, worker ID, action, dependencies, acceptance criteria and budget. Never include secrets.

## Step 7 — Plan and validate
Run `python aisdf.py plan --project ../your-project --tasks examples/tasks.example.json`. The planner checks worker existence, allowed/requested action categories, dependency references/cycles and task budgets. It writes `.aisdf/workforce-plan.json` and records events in SQLite.

## Step 8 — Human approval
Review each task, exact scope, risk and budget. Approve using `python aisdf.py approve --project ../your-project --task-id TASK-ID --approver "Your Name"`. Approval is recorded against the task digest. Do not approve work you have not reviewed.

## Step 9 — Execute through an authorized operator or adapter
The 1.0 runtime has no model provider. It can (a) run an approved `execute` task as a governed local command (`python aisdf.py run`, allow-listed executables only, evidence recorded, **not a sandbox**) or (b) record a human-performed task with an evidence file (`python aisdf.py complete`). Before either, move the task to READY with `transition --to READY`; this re-verifies the approval and the dependencies. A future/provider adapter must implement `runtime/adapters/WORKER-ADAPTER-CONTRACT.md`, pass security tests, and use an external OS-level sandbox for untrusted code. The runtime deliberately refuses to mark work RUNNING without an actual execution adapter.

## Step 10 — Verify independently
Run tests and applicable security, performance, accessibility, compatibility and regression checks. Record exact commands, outputs, artifacts and unrun checks. A reviewer must be independent of the implementation context for high-risk changes.

## Step 11 — Release decision
The human release owner reviews acceptance criteria, unresolved findings, approvals, rollback and residual risk. A worker cannot self-approve or self-release.

## Step 12 — Maintain project truth
Update `PROJECT.md`, `AGENTS.md`, decisions, findings and change history only from verified evidence. Re-run repository and project checks.

## Step 13 — Extend safely
Add a new worker by creating a role contract and manifest, validating its schema, writing contract tests, and only then registering an execution adapter. Promote maturity from L1 to L2/L3/L4 only with evidence.


## Steps 10–11 with the 1.0 tools
- Record checks: `python aisdf.py check run --project P --id unit-tests --tool unittest -- python -m unittest` (runtime-executed) or `check record` for results produced elsewhere (needs the tool's real output file).
- Independent review: `python aisdf.py review-package --project P --out ../review-pkg`, give it to a fresh read-only reviewer, then `findings add` their schema-valid findings.
- Dispositions: only a registered human, with rationale/evidence: `python aisdf.py findings resolve ...`.
- Release gate: `python aisdf.py gate --project P`. BLOCKED lists every reason. PASS means the evidence satisfies the policy, not that the software is proven secure.
- Integrity: `python aisdf.py verify-ledger --project P`.

See `RULES-AND-ENFORCEMENT.md` for exactly what is enforced.
