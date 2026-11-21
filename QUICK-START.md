# Quick Start

1. Clone/download this repository and read the root `README.md`.
2. Read [`examples/EXAMPLE-AI-SAAS-PROJECT.md`](examples/EXAMPLE-AI-SAAS-PROJECT.md) once. Then copy [`project.md`](project.md) into your own project folder and fill in at least the identity, problem statement, existing-solutions check, solution and functionalities sections.
3. Choose a mode in `modes/` (Problem Discovery, New Project, or Existing Project X-Ray).
4. Optionally copy `templates/PROJECT-PROFILE.template.yaml` into the project workspace and fill known fields.
4a. Run the Appendix B checklist in `project.md` (prompt C1) before approving the baseline.
5. Give your AI tool `project.md` and `prompts/MASTER-ENTRY-PROMPT.md` (or paste starter prompt A1 from the bottom of `project.md`).
6. Ask the tool to list facts, decisions, assumptions, unknowns, risks and required approvals before implementation.
7. Select the workflow in `workflows/` and reference the relevant engine specs.
8. Create work units from `schemas/work-unit.schema.json` (or the work-unit table in `project.md`) and track checkpoints/handoffs.
9. Execute only authorized actions. Capture command output, test reports, commits and review records.
10. Update Section 17 (Status and Handoff) of `project.md` after every task.
11. Close with `schemas/completion-report.schema.json`; do not claim deployment unless deployment evidence exists.

AISDF does not execute these steps itself. The selected AI tool and authorized environment do.
