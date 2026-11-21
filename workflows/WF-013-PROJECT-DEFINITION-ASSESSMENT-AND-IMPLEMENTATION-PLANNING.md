# WF-013 — Project Definition, Existing-System Assessment, and Implementation Planning

## Purpose
Create and maintain a single `PROJECT.md` source of truth for a target software project; inspect the real repository; identify missing, conflicting, unverified, and implemented capabilities; obtain explicit human approvals; and produce a traceable implementation plan and execution prompt.

## Required behavior
1. **Connect to the actual target repository.** Confirm the absolute root, Git state/revision, current branch, and available files. Never assess only a pasted description when a repository is available.
2. **Read instruction hierarchy first.** Inspect existing `AGENTS.md`, `CLAUDE.md`, `.cursor/rules/`, `.agents/rules/`, Antigravity workspace instructions, and relevant nested instruction files. Preserve existing rules; do not overwrite them.
3. **Read existing project truth.** Inspect README/docs, manifests, source, tests, migrations, CI, deployment files, API contracts, and changelog. Do not expose secret values. Record inaccessible areas.
4. **Build evidence-backed inventory.** Map features to code/docs/tests and label each `IMPLEMENTED_VERIFIED`, `IMPLEMENTED_UNVERIFIED`, `PARTIAL`, `DOCUMENTED_ONLY`, `PLANNED`, `MISSING`, `CONFLICTING`, or `UNKNOWN`.
5. **Draft or update PROJECT.md.** Preserve user-authored and approved content. Use source citations as repository-relative file/line references, Git revision, command evidence, or external source links. Never overwrite without diff/backup and approval.
6. **Challenge requirements.** Detect vague problem statements, missing personas, feature gaps, hidden workflows, role/permission gaps, edge cases, NFR gaps, security/privacy risks, data lifecycle gaps, acceptance criteria gaps, and conflicting requirements. Separate facts, inferences, assumptions, recommendations, and questions.
7. **Create findings.** Each finding gets stable ID, severity, impact, evidence, confidence, recommended action, owner, and disposition state. Deduplicate without discarding dissent.
8. **Generate implementation plan.** Group approved work into dependency-aware phases and work units; specify exact files likely to change, migrations, tests, risks, rollback, and acceptance criteria. Mark unapproved scope as proposed.
9. **Human approval gate.** Stop before modifying application source. Require approval of the problem statement, requirements, scope, architecture where relevant, and exact implementation plan/file allowlist. A generic “yes” is not authorization for unspecified destructive or external actions.
10. **Generate an execution prompt.** Only after explicit plan approval. Prompt must point the agent to `PROJECT.md`, `AGENTS.md`, the approved plan, scope allowlist, and relevant tests. It must require pre-change inspection, minimal diffs, tests, drift check, and truthful completion report.
11. **Implement in the real repository.** The host AI agent performs implementation under the approved scope and tool permissions. AISDF runtime only generates/validates planning artifacts; it does not edit application source.
12. **Verify and reconcile.** Compare actual Git changes against allowlist, map implementation to requirement/AC IDs, run authorized checks, update `PROJECT.md` statuses and findings, and report residual gaps.

## Output artifacts
- `PROJECT.md` — canonical project definition and approved requirements.
- `.aisdf/assessment/EXISTING-PROJECT-ASSESSMENT.md` — repository inspection, feature status, evidence, coverage and gaps.
- `.aisdf/findings/` — structured findings.
- `.aisdf/plans/IMPLEMENTATION-PLAN-<ID>.md` — dependency-aware plan and exact file allowlist.
- `.aisdf/prompts/IMPLEMENTATION-PROMPT-<ID>.md` — generated only after plan approval.
- `.aisdf/reports/` — validation, drift and completion reports.

## Status vocabulary
`DRAFT`, `NEEDS_INFORMATION`, `READY_FOR_REVIEW`, `APPROVED`, `REJECTED`, `BLOCKED`, `IN_PROGRESS`, `VERIFIED`, `CLOSED`.

## Acceptance criteria
- Every material claim is evidence-linked or explicitly labeled unknown/inference.
- Existing feature status is not inferred from README claims alone; code and tests are inspected where available.
- Missing functions/features and conflicts are explicit.
- Approval is attributable to a human and a specific artifact revision.
- Implementation prompt cannot be generated for an unapproved plan.
- The workflow is non-destructive until approved; source edits are performed by the connected host agent, not the planner CLI.
