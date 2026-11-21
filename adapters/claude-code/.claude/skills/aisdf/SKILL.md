---
name: aisdf
description: Execute AISDF WF-007 through WF-012 for concept evaluation, design specifications, independent reviews, finding resolution, codebase mapping, and specification drift.
---

# AISDF workflow skill

1. Read the AISDF governance rulebook and the EGM-inspired workflow docs in this repository before acting.
2. Use the portable runtime at `UPGRADES/EGM-INSPIRED-SPEC-DRIVEN-ENGINEERING/runtime/tools/aisdf.py` (or the installed project copy under `.aisdf-tools/`).
3. Execute only the workflow requested. Create artifacts before implementation.
4. WF-009: delegate reviewers to genuinely fresh subagent contexts with only the approved spec and explicitly allowed references. Do not pass the parent conversation. Record each session identifier and evidence. If isolation cannot be proven, mark `NON_INDEPENDENT` or `BLOCKED`.
5. Do not edit application source until a human approves the spec and its exact file allowlist. Never expand the allowlist silently.
6. After approved implementation, run tests, add findings, resolve with evidence, and generate drift report.
7. Report what was specified, executed, tested, independently reviewed, and not verified.
