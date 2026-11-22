# Release Validation — AISDF 3.8.3

- Validation date: 2026-11-21
- Scope: repository structure, project lifecycle CLI, documentation links, schema validation, tests, and demo artifact generation.
- Environment: local Python 3.13 runtime in the build environment; project declares Python 3.10+ compatibility.

## Results

| Check | Result | Evidence |
|---|---|---|
| Repository validator | PASS | `python tools/validate_repository.py` |
| Engine contracts | PASS — 56 numbered specs | repository validator |
| JSON schemas | PASS — 9 schemas | Draft 2020-12 meta-validation |
| JSON fixtures | PASS — 2 fixtures parse and mapped fixtures conform | repository validator |
| Internal Markdown links | PASS | repository validator |
| Required root files/templates/license | PASS | repository validator |
| Automated test suite | PASS — 14 tests | `python -m pytest -q` |
| Project CLI help | PASS | `python tools/aisdf_runtime/project.py --help` |
| AISDF EGM runtime help | PASS | `python tools/aisdf_runtime/aisdf.py --help` |
| CLI demo screenshots | GENERATED | `docs/demo/assets/` from actual local CLI stdout/stderr |

## Project lifecycle behavior covered

- Default initialization creates `PROJECT.md`, `AGENTS.md`, and `.aisdf/` folders.
- Existing `PROJECT.md` is never overwritten.
- Existing `AGENTS.md` is preserved.
- `--no-agents` is available as an explicit opt-out.
- `check` validates 25 required sections, metadata, status vocabulary, duplicate IDs, required inventory/traceability fields, internal PROJECT.md links, and required AGENTS policy sections.
- A blank template reports `INCOMPLETE`; `--strict` returns non-zero while warnings remain.
- Assessment inventory, plan creation, approval digest, and approval-gated prompt generation are covered by lifecycle tests.

## Known limitations

- The document checker validates structure and basic consistency, not semantic truth or project completeness.
- The inventory command is deterministic file discovery, not feature understanding.
- Semantic assessment requires a connected AI agent inspecting the actual repository and citing evidence.
- The approval digest detects plan-body changes but does not authenticate the identity of the person who entered approval fields.
- AI host adapters have not been live-certified; no LLM invocation, autonomous agent spawning, or production deployment is claimed.
- Maintainers must confirm rights to all original and third-party assets before public redistribution under the MIT license.

## Reproduction

```bash
python -m pip install -r requirements-dev.txt
python tools/validate_repository.py
python -m pytest -q
python tools/aisdf_runtime/project.py --help
python tools/aisdf_runtime/aisdf.py --help
```
