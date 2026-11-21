# Demo execution record

The PNGs in this directory are terminal-style screenshots rendered from the actual stdout/stderr of the AISDF project lifecycle CLI during a local run on 2026-11-21. The temporary project is synthetic (`Tiny Notes Demo`) and was created only for this walkthrough. The approval in step 4 is a demo fixture, not an approval for any external repository.

Screenshots:
1. `01-project-init.png` — CLI creates PROJECT.md, AGENTS.md, and .aisdf workspace.
2. `02-repository-assessment.png` — CLI creates deterministic repository inventory.
3. `03-project-definition-check.png` — CLI checks structure and reports draft placeholders.
4. `04-plan-approval.png` — CLI computes the approval digest; demo plan records a synthetic approval.
5. `05-approved-implementation-prompt.png` — CLI generates a prompt only after digest and allowlist checks pass.

The CLI does not perform semantic code review or implementation.
