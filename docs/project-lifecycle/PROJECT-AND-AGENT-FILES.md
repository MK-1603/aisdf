# PROJECT.md and AGENTS.md — How AISDF Uses Them

## Two different responsibilities

- `PROJECT.md` is the project's **product and engineering source of truth**: why it exists, who it serves, problem statement, behavior, features, requirements, constraints, architecture, acceptance criteria, decisions, gaps, and approval state.
- `AGENTS.md` is the **operating contract for AI coding agents**: how to work in the repository, which documents to read, commands to run, safety boundaries, code conventions, and reporting requirements.
- `README.md` is the **human-facing introduction**. It is not a substitute for either file.

Do not put the full PRD in AGENTS.md. Keep AGENTS.md short and point to PROJECT.md and detailed docs. Keep project-specific truth out of global personal agent instructions.

## Recommended target-project layout

```text
my-project/
├── README.md
├── PROJECT.md                 # canonical project definition
├── AGENTS.md                  # shared coding-agent contract
├── CLAUDE.md                  # optional Claude bridge: @AGENTS.md
├── .cursor/rules/aisdf.mdc    # Cursor-specific loading rule
├── .agents/rules/aisdf.md     # Antigravity-specific loading rule
├── docs/                      # detailed specs / ADRs / runbooks
└── .aisdf/
    ├── assessment/
    ├── findings/
    ├── plans/
    ├── prompts/
    ├── reports/
    └── runtime-manifest.json
```

## Agent session protocol

1. Resolve repository root and read the nearest applicable instruction files.
2. Read PROJECT.md and check its status/revision/approval state.
3. Read the active task plan and its exact file allowlist.
4. If the task is assessment-only, remain read-only.
5. If plan approval is missing or stale, stop before source edits.
6. Implement only approved work; ask before scope expansion.
7. Run required tests and report exact commands/results.
8. Update requirement/feature status and evidence, then report residual gaps.

## Provider notes (verify against installed host version)

- Codex: use root/nested `AGENTS.md` as the primary project instruction file.
- Cursor: use `AGENTS.md` plus `.cursor/rules/*.mdc` for Cursor-specific rules.
- Antigravity: package workspace `AGENTS.md`/`GEMINI.md` and `.agents/rules/` as appropriate; verify discovery in the installed version.
- Claude Code: use `CLAUDE.md` as its native project instruction entry point. A minimal `CLAUDE.md` containing `@AGENTS.md` shares the common contract. Do not assume Claude will always load AGENTS.md automatically; behavior depends on version and instruction settings.

## Safety
Never overwrite an existing README, PROJECT.md, AGENTS.md, CLAUDE.md, or provider rules without first reading it and showing a proposed diff. Merge additions; preserve local rules. Never put secrets in these files.
