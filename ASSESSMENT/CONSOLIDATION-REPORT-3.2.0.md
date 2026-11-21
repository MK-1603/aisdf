# Consolidation Report — AISDF 3.2.0

Date: 2026-11-21. Scope: local comparison of four supplied packages and the build of one consolidated package. This is a repository-artifact review only.

## Inputs compared
| Package | Files | Role in consolidation |
|---|---|---|
| `AISDF_V3_Repository_Starter` | 59 | Source of fuller governance/protocol text, `CITATION.cff` |
| `AISDF_Complete_GitHub_Repository_v3_0_0-foundation` | 180 | Superseded; engine filenames contained commas |
| `AISDF_Complete_GitHub_Repository_v3_0_1-governance` | 200 | Source of unique policies, standards and checklists |
| `AISDF_Complete_GitHub_Repository_v3_1_0-validation` | 199 | **Base**: engine contracts, validator, tests, DevTrack spec, assessment |

## What was kept, merged or dropped
| Item | Decision | Reason |
|---|---|---|
| v3.1.0 tree | Kept as base | Newest; validator and tests pass; normalized engine filenames |
| v3.0.1 `AISDF-DEFINITIONS`, five policies, `CONTRIBUTION-RULES`, `FILE-NAMING-STANDARDS`, `FILE-FORMAT-STANDARDS`, two checklists | Merged into `00-GOVERNANCE/` (flat layout) | Not present in 3.1.0; policies keep status PROPOSED |
| v3.0.1 nested `FOUNDATION/`, `RULES/`, `COMPLIANCE/` folders | Not carried as folders | 3.1.0 already has flat equivalents (mission, principles, documentation, engine, schema, workflow, release rules, exception register); the flat 3.1.0 files were kept |
| Starter fuller text (rulebook extras, handoff and completion protocols, freshness policy, tool-capability and standards files, `SECURITY.md`, Mode 1) | Appended as "Additional detail" | 3.1.0 had shortened these; no text was deleted |
| Starter `CITATION.cff` | Kept, version set to 3.2.0 | Not in 3.1.0 |
| Starter `ENGINE-CATALOGUE.md`, `engine-registry.yaml`, `rule-registry.yaml` | Dropped | Superseded by `engines/README.md` and `registries/*.md`; the YAML files were starter-stage and incomplete |
| `project.md` and new `README.md` | Added | Requested deliverables |

## Defects found
| Defect | Action |
|---|---|
| 28 of the domain `README.md` titles and topic text did not match their folder names (for example `08-SOFTWARE-ARCHITECTURE` was titled "Ai And Model Intelligence") | Fixed |
| v3.0.0/3.0.1 engine filenames contained commas | Already fixed in 3.1.0; confirmed |
| v3.0.1 changelog still said 3.0.0 | Corrected in the version history |
| The starter rulebook has a different set of 20 rules than 3.1.0 (it includes No Fake Execution, Git Safety, Handoff Completeness; 3.1.0 includes Scope Lock, Privacy by Design, Independent Verification) | 3.1.0 list kept as canonical; the three starter-only items are recorded as supplementary requirements. Maintainers should decide whether to renumber |
| `registries/RULE-REGISTRY.md` does not list individual rules | Not changed |
| Review cadences differ slightly between the starter and 3.1.0 freshness policy | Both retained as defaults; maintainers should pick one |

## Verification run (local)
- `python tools/validate_repository.py`: PASS (56 engines, 8 schemas, 2 fixtures, required files including `project.md` and `CITATION.cff`, internal Markdown links).
- `python -m pytest`: 2 passed.
- Final zip was extracted to a clean folder and the same two commands were run there.

## Not verified
Remote CI execution, external tool adapters, the DevTrack application, legal/licensing readiness, and the quality of each engine's content beyond structure. The 56 engine files are similar in size and share a common contract layout; their domain content has not been independently reviewed.
