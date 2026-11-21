# Quick Start

1. Clone/download this repository and read the root README.
2. Choose a mode in `modes/`.
3. Copy `templates/PROJECT-PROFILE.template.yaml` into the project workspace and fill known fields.
4. Run the master prompt from `prompts/MASTER-ENTRY-PROMPT.md` in your selected AI tool.
5. Provide the relevant project documents and repository context.
6. Ask the tool to list facts, decisions, assumptions, unknowns, risks and required approvals before implementation.
7. Select the workflow in `workflows/` and reference the relevant engine specs.
8. Create work units from `schemas/work-unit.schema.json` and track checkpoints/handoffs.
9. Execute only authorized actions. Capture command output, test reports, commits and review records.
10. Close with `schemas/completion-report.schema.json`; do not claim deployment unless deployment evidence exists.

AISDF does not execute these steps itself. The selected AI tool and authorized environment do.


## Define and assess a real project (WF-013)

From the AISDF repository, initialize the target project workspace (the helper refuses to overwrite existing files):

```bash
python tools/aisdf_runtime/project.py init --project ../my-project --name "My Project" --add-agents
python tools/aisdf_runtime/project.py assess --project ../my-project
python tools/aisdf_runtime/project.py plan-create --project ../my-project --id P001 --title "First approved improvement"
```

Use `prompts/PROJECT-ASSESSMENT-ENTRY-PROMPT.md` with ChatGPT, Claude, Codex, Cursor, or Antigravity while the agent is connected to the actual target repository. The assessment command creates a deterministic file inventory only; the connected AI agent must inspect source and tests to complete semantic feature mapping and missing-gap analysis.

After filling the plan and exact file allowlist, compute its approval digest:

```bash
python tools/aisdf_runtime/project.py plan-hash --project ../my-project --plan IMPLEMENTATION-PLAN-P001.md
```

An authorized human must record `APPROVED`, approver, date, and the exact digest in the plan's approval block. Only then can the execution prompt be generated:

```bash
python tools/aisdf_runtime/project.py prompt-create --project ../my-project --plan IMPLEMENTATION-PLAN-P001.md
```

The runtime does not edit application source. The connected coding agent reads `PROJECT.md`, `AGENTS.md`, and the approved plan, implements only the allowlisted changes, and runs the planned verification.
