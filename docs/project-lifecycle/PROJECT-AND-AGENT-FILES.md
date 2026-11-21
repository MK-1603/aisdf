# PROJECT.md and AGENTS.md — Project Source of Truth and Agent Contract

## Why two files?

- `PROJECT.md` defines **what the project is and how it should behave**: problem, evidence, actors, functions/features, requirements, journeys, domain rules, data, architecture, integrations, UX, security, scope, acceptance criteria, gaps, risks, operations, decisions, approvals, and traceability.
- `AGENTS.md` defines **how an AI agent may work in the repository**: reading order, evidence rules, pre-flight, scope, approval, security, testing, Git safety, documentation maintenance, completion reports, and stop conditions.
- `README.md` is the human-facing introduction and setup guide.

Do not put the full product specification in AGENTS.md. Keep AGENTS.md an operational policy and PROJECT.md the project truth.

## Generate the files for a project

Run from the AISDF repository root:

```bash
python tools/aisdf_runtime/project.py init --project ../my-project --name "My Project" --type DEMO
```

By default, it creates both `PROJECT.md` and `AGENTS.md`, plus `.aisdf/assessment`, `findings`, `plans`, `prompts`, `reports`, and `context`. Existing files are preserved. The command refuses to overwrite an existing `PROJECT.md`; if `AGENTS.md` exists, it is preserved and the generated policy is not merged automatically. Use `--no-agents` to opt out of AGENTS generation.

## What PROJECT.md checks

The reusable template has 25 sections:

1. Executive summary
2. Full problem statement and evidence
3. Purpose, vision, objectives, and outcomes
4. Users, actors, and stakeholders
5. Existing repository and system baseline
6. Complete feature and function inventory
7. User journeys and operational workflows
8. Functional requirements
9. Non-functional requirements
10. Domain rules and application logic
11. Data model and information lifecycle
12. Architecture and technical design
13. Technology stack and dependencies
14. API, integration, and interface contracts
15. UX, UI, accessibility, and documentation
16. Security, privacy, safety, and abuse cases
17. Scope and constraints
18. Acceptance criteria and verification matrix
19. Missing functionality, defects, conflicts, and open questions
20. Risks and mitigations
21. Build, test, release, operations, and support
22. Project-specific agent rules and permissions
23. Decisions and approval gates
24. Implementation plan and traceability
25. Change history

For an open-source library, a demo, or a college project, fill relevant sections and mark irrelevant ones `NOT_APPLICABLE` with a reason. Do not invent revenue, customers, deployment, or business metrics.

## Feature status vocabulary

- `IMPLEMENTED_VERIFIED`
- `IMPLEMENTED_UNVERIFIED`
- `PARTIAL`
- `DOCUMENTED_ONLY`
- `PLANNED`
- `MISSING`
- `BROKEN`
- `UNKNOWN`
- `NOT_APPLICABLE`

`IMPLEMENTED_VERIFIED` requires evidence from an executed test or reproducible behavior. Documentation or file presence alone is insufficient.

## Run the project document checker

```bash
python tools/aisdf_runtime/project.py check --project ../my-project
```

The checker validates required headings, metadata markers, status vocabulary, duplicate feature/acceptance IDs, and required AGENTS policy sections. It warns while a project template still has placeholders or draft status. Add `--strict` to fail while warnings remain, or `--json` for machine-readable results.

This is a structural checker. It cannot judge whether the project statement is accurate, whether feature mapping is complete, or whether a test proves user behavior. A connected AI agent and human reviewer must complete that semantic assessment.

## Existing project assessment

```bash
python tools/aisdf_runtime/project.py assess --project ../my-project
```

This writes a deterministic file inventory under `.aisdf/assessment/`. Then connect an AI coding environment to the actual repository and use `prompts/PROJECT-ASSESSMENT-ENTRY-PROMPT.md`.

The agent must inspect source code, tests, documentation, manifests, migrations, APIs, permissions, integrations, CI, deployment, and security. Each finding must cite file paths/lines, tests, command output, or reproducible behavior. Unknowns stay unknown.

## Plan and approval lifecycle

```bash
python tools/aisdf_runtime/project.py plan-create --project ../my-project --id P001 --title "Improve feature X"
python tools/aisdf_runtime/project.py plan-hash --project ../my-project --plan .aisdf/plans/IMPLEMENTATION-PLAN-P001.md
python tools/aisdf_runtime/project.py prompt-create --project ../my-project --plan .aisdf/plans/IMPLEMENTATION-PLAN-P001.md
```

The human fills the plan and exact file allowlist, computes the digest, then records explicit approval, approver, date, digest, and approved file list. If the plan changes, re-hash and re-approve. Prompt generation is blocked if required approval evidence or the digest is invalid.

The digest is an integrity check on the plan body, not a cryptographic identity/signature of the human. The runtime cannot authenticate who typed the approval fields.

## AI session protocol

1. Resolve repository root and read applicable instructions.
2. Read PROJECT.md and check its status and revision.
3. Read the active approved plan and verify its digest.
4. Inspect code and tests before editing.
5. Stay inside the exact file allowlist.
6. Ask before scope expansion or destructive/external/paid/production actions.
7. Run relevant checks and record exact outcomes.
8. Update PROJECT.md only with verified facts and approved decisions.
9. Report changed files, evidence, unrun checks, and remaining gaps.

## Host-specific notes

- Codex: use `AGENTS.md` as the repository instruction source where supported.
- Claude Code: include a root `CLAUDE.md` bridge with `@AGENTS.md` if desired; verify installed-version behavior.
- Cursor: retain `AGENTS.md` and add `.cursor/rules/*.mdc` as needed.
- Antigravity: use supported workspace instruction and `.agents/rules/`/skills structures for the installed version.

Do not assume every host automatically loads every generic file. Test the adapter in the actual host.
