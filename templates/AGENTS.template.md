# Project Agent Instructions

## Source of truth
- Read `PROJECT.md` before product, architecture, or feature work.
- Read the active approved plan under `.aisdf/plans/` before implementation.
- `README.md` is introductory; it does not override PROJECT.md or this file.

## Workflow
- Confirm repository root, branch, and working-tree state before changes.
- Inspect existing code and tests before proposing edits.
- Follow existing architecture and conventions unless an approved plan changes them.
- Keep changes within the approved plan's exact file allowlist. Stop and request approval for scope expansion.
- Never invent requirements, claim unrun tests, or silently mark a feature complete.

## Safety
- Never expose or commit secrets, credentials, private keys, or production data.
- Do not run destructive commands, migrations against production, deployment, push, merge, or external communications without explicit authorization.
- Preserve existing instructions and user changes. Do not overwrite files without reviewing their contents and proposing a diff.

## Verification and reporting
- Run the project's documented checks relevant to the change.
- Record exact commands and actual outcomes; distinguish PASS, FAIL, NOT_RUN, and BLOCKED.
- Map changes to PROJECT.md requirement and acceptance-criterion IDs.
- Report changed files, tests, limitations, residual findings, and approval references.
