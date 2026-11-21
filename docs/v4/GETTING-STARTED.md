# Getting Started — Step by Step

## 1. Validate AISDF
`python tools/validate_repository.py`

## 2. Run tests
`python -m unittest discover -s tests -v`

## 3. Initialize your project
`python runtime/aisdf_runtime/workforce.py init --project ../my-project --name "My Project"`

## 4. Inspect the project
Use `python tools/aisdf_runtime/project.py assess --project ../my-project`, then ask a connected coding assistant or human engineer to inspect code and fill the semantic assessment with evidence.

## 5. Define requirements
Complete PROJECT.md; run the PROJECT.md checker; do not treat placeholders as approved facts.

## 6. Build a work-unit file
Copy `examples/tasks.example.json` and edit worker IDs, dependencies, action, budgets and acceptance criteria.

## 7. Validate and plan
Run the workforce `plan` command. It validates worker IDs, action policy, dependency DAG and budget.

## 8. Approve
A named human approves each task in the local ledger. Approval records include the planned task digest.

## 9. Execute
This release does not ship an LLM executor. Assign the task to a human or configure a conforming adapter and external sandbox. Never mark a task RUNNING without a real execution integration.

## 10. Verify and close
Record evidence, test output, findings, reviewer decision and completion status. Update PROJECT.md only from verified facts.
