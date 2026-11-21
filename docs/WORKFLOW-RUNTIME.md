# WF-007–WF-012 Runtime Guide

## Requirements
Python 3.10+. Git is required for drift reports. The runtime uses only the Python standard library.

## Commands
Run `python tools/aisdf_runtime/aisdf.py --help` for the complete CLI.

```bash
python tools/aisdf_runtime/aisdf.py init --project ../my-project
python tools/aisdf_runtime/aisdf.py challenge --project ../my-project --title "Example capability"
python tools/aisdf_runtime/aisdf.py spec-create --project ../my-project --title "Example capability" --id SPEC-001
python tools/aisdf_runtime/aisdf.py validate-spec --spec ../my-project/.aisdf/specs/SPEC-001.md
python tools/aisdf_runtime/aisdf.py review-init --project ../my-project --spec-id SPEC-001
python tools/aisdf_runtime/aisdf.py bootstrap --project ../my-project
python tools/aisdf_runtime/aisdf.py drift --project ../my-project --spec ../my-project/.aisdf/specs/SPEC-001.md
```

Additional commands include `review-stage`, `review-independence`, `review-validate`, `finding-add`, and `finding-resolve`.

## Safety and limits
- Runtime-generated artifacts are drafts; humans approve decisions.
- The runtime does not call model APIs, launch agents, or edit application source files.
- Independent-review status is recorded from operator-supplied evidence; the runtime cannot inspect whether a host truly isolated reviewer context.
- Drift checks compare Git working-tree paths with the specification allowlist. They do not establish semantic correctness.
- Host adapters provide instructions and native discovery files; no live host certification is claimed.

## WF-013 project lifecycle helper

The companion `project.py` CLI creates a target project's `PROJECT.md` source of truth and `.aisdf/` workspace, creates a deterministic repository inventory, scaffolds implementation plans, computes a digest for human approval, and generates an execution prompt only after the plan is approved and its content digest matches.

```bash
python tools/aisdf_runtime/project.py init --project ../my-project --name "My Project" --add-agents
python tools/aisdf_runtime/project.py assess --project ../my-project
python tools/aisdf_runtime/project.py plan-create --project ../my-project --id P001 --title "Approved improvement"
python tools/aisdf_runtime/project.py plan-hash --project ../my-project --plan .aisdf/plans/IMPLEMENTATION-PLAN-P001.md
python tools/aisdf_runtime/project.py prompt-create --project ../my-project --plan .aisdf/plans/IMPLEMENTATION-PLAN-P001.md
```

Before `prompt-create`, an authorized human must set `Approval status: APPROVED`, name the approver, enter the approval date, and copy the digest returned by `plan-hash` into the plan's approval block. The digest covers the plan body outside the approval block, so changing scope, tasks, tests, or file allowlist invalidates the approval. Recompute and re-approve after any plan-body edit.

`assess` is deterministic inventory only. It does not inspect semantic behavior or infer whether features work. The connected AI coding environment must inspect actual source and tests using `prompts/PROJECT-ASSESSMENT-ENTRY-PROMPT.md`. The runtime never modifies application source, and it does not call ChatGPT or Claude APIs.
