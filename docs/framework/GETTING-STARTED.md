# Getting Started — Step by Step

## 1. Validate AISDF
`python tools/validate_repository.py`

## 2. Run tests
`python -m unittest discover -s tests -v`

## 3. Initialize your project
`python aisdf.py init --project ../my-project --name "My Project" --owner "Your Name"` (run in a real terminal; this registers you as the first human approver)

## 4. Inspect the project
Use `python tools/aisdf_runtime/project.py assess --project ../my-project`, then ask a connected coding assistant or human engineer to inspect code and fill the semantic assessment with evidence.

## 5. Define requirements
Complete PROJECT.md; run the PROJECT.md checker; do not treat placeholders as approved facts.

## 6. Build a work-unit file
Copy `examples/tasks.example.json` and edit worker IDs, dependencies, action, budgets and acceptance criteria.

## 7. Validate and plan
Run `python aisdf.py plan --project ../my-project --tasks tasks.json`. It validates worker IDs, action policy, dependency DAG, budget and (for `execute` tasks) the argv command.

## 8. Approve
A **registered** human approves each task (`approve`). The approval is bound to the task's content digest and recorded with its assurance level; changing the task revokes it.

## 9. Execute
There is no LLM executor. Move the task to READY (`transition --to READY`, which re-checks approval and dependencies), then either run an allow-listed local command (`run`, evidence recorded, not a sandbox) or have a human do it and record it with `complete --evidence`. Never mark a task SUCCEEDED without evidence; the runtime refuses.

## 10. Verify and close
Record checks (`check run` / `check record`), build the reviewer package (`review-package`), add findings (`findings add`), have a registered human disposition them, then run `python aisdf.py gate`. Update PROJECT.md only from verified facts.
