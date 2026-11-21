# Changelog

## 3.3.0 — Worked example and check/update routine — 2026-11-21
- Added `examples/EXAMPLE-AI-SAAS-PROJECT.md`: a complete filled-in `project.md` for a simple AI SaaS, with an existing-solutions check (Otter.ai, Fireflies.ai, manual chatbot) sourced and dated 2026-11-21; third-party figures are labelled unverified.
- Added Appendix B (baseline completeness checklist) and Appendix C (check-and-update routine, prompts C1–C3) to `project.md`.
- Updated README, QUICK-START, templates and examples guides; validator now requires the example file.
- Not changed: the example app has not been built; no license selected; no adapters certified.

## 3.2.0 — Consolidated build — 2026-11-21
- Based on 3.1.0 after comparing the starter, 3.0.0, 3.0.1 and 3.1.0 packages.
- Added `project.md`: a single downloadable project brief (problem statement, existing-solutions check, solution, functionalities, upgrade analysis, building plan, AI rules, starter prompts).
- Rewrote the root `README.md` as a global guide with names, usage paths and honest status.
- Merged unique files from 3.0.1 into `00-GOVERNANCE/`: definitions, change-management, deprecation, privacy, security and versioning policies, contribution rules, file-naming and file-format standards, governance-review and release-readiness checklists.
- Added `CITATION.cff` (from the starter, updated to 3.2.0).
- Restored detail that 3.1.0 had condensed: the starter's fuller text is appended to 19 governance, protocol and checklist files, to the rulebook (supplementary requirements, application, preflight, completion), to `SECURITY.md` and to Mode 1.
- Master entry prompt now reads `project.md` first when present; validator now requires `project.md` and `CITATION.cff`.
- Fixed 28 domain README titles and topic text that did not match their folder names.
- Added `ASSESSMENT/CONSOLIDATION-REPORT-3.2.0.md`.
- Not changed: no license selected, no adapters certified, DevTrack not implemented, remote CI not run.

## 3.0.0-foundation — 2026-11-21
- Expanded the starter into a canonical repository structure.
- Added 56 engine specification files, 31 domain directories, three modes and four workflows.
- Added governance standards, role/phase prompts, templates, eight JSON Schemas, fixtures and a repository validator.
- Added GitHub Actions validation workflow; it has not been run on a remote GitHub repository in this build.
- No external tool adapters are certified; no reference application has been built/deployed as proof.

## 3.1.0 — Reference validation foundation
- Added engine-specific execution contracts and minimum test scenarios to all 56 engine specifications.
- Added documentation, engine, workflow, schema and release governance standards.
- Added DevTrack reference-project specification and validation plan (application not implemented).
- Added evidence-based maturity rubric and release-readiness checklist.
- Strengthened repository validation and added pytest checks.
- Normalized punctuation in engine filenames.
