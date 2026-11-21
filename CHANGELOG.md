# Changelog

## 3.8.2 — 2026-11-21
- Integrated the MK Framework as an optional venture-to-software methodology under `01-METHODOLOGY/MK-FRAMEWORK/`.
- Added the complete written method, stage-by-stage gate guidance, evidence/decision-record requirements, and connection points to AISDF workflows.
- Added the MK Framework overview infographic and linked it from the global README and documentation index.
- Kept venture validation separate from AISDF engineering governance; the MK Framework does not replace human approvals, security, or verification controls.


## 3.8.1 — 2026-11-21
- Added root `PROJECT.md` defining AISDF itself and strengthened root `AGENTS.md` with project-source-of-truth behavior.
- Added WF-013 for project definition, existing-repository assessment, gap analysis, human approvals, implementation planning, and execution prompt generation.
- Added reusable `PROJECT.md` and `AGENTS.md` templates, project assessment prompt, provider instruction bridges, and project lifecycle documentation.
- Added portable project helper CLI: init, deterministic assess, plan-create, plan-hash, and approval-gated prompt-create.
- Added tests for non-overwrite behavior and approval-gated prompt generation.

## 3.8.0 — Repository consolidation and usability release

- Flattened the deliverable so the repository root is the actual AISDF project, not a wrapper containing a second `AISDF/` directory.
- Added a global root `README.md` explaining purpose, operating model, lifecycle, repository map, quick start, validation, and maturity limits.
- Promoted WF-007–WF-012 into the main workflow directory and placed the CLI in `tools/aisdf_runtime/`.
- Added a documentation index and runtime guide.
- Consolidated Claude Code, Codex, Cursor, and Antigravity adapters under `adapters/`.
- Added repository-level `AGENTS.md` guidance and updated version metadata.
- Preserved honest capability statements: no LLM invocation, autonomous reviewer isolation, host certification, or production app is claimed.
