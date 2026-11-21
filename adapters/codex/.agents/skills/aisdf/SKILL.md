---
name: aisdf
description: Run AISDF WF-007–WF-012 as repeatable spec-driven engineering workflows with artifact validation and evidence-based gates.
---

# AISDF for Codex

- Read root `AGENTS.md` and the AISDF workflow documents first.
- Use `tools/aisdf.py` from the AISDF runtime.
- Produce durable artifacts in `.aisdf/`; do not keep the only copy in chat.
- For independent review, use separate subagent sessions only when the active Codex environment exposes them. Give reviewers the approved spec and permitted source material, not the originating discussion. Capture evidence. Otherwise set status to `NON_INDEPENDENT` or `BLOCKED`.
- Human approval is mandatory before source edits. Respect the exact file allowlist.
- Run project tests and `aisdf.py drift` after implementation. Distinguish test results from review opinions.
