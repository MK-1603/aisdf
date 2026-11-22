# Release Validation — AISDF 3.8.2

Date: 2026-11-21

## Changes validated

- MK Framework written methodology added under `01-METHODOLOGY/MK-FRAMEWORK/`.
- MK Framework infographic included at `01-METHODOLOGY/MK-FRAMEWORK/assets/MK-FRAMEWORK-OVERVIEW.png`.
- Root README and documentation index link to the methodology and visual.
- Version and manifest updated to 3.8.2.

## Checks executed

| Check | Result |
|---|---|
| `python tools/validate_repository.py` | PASS |
| `python -m pytest -q` | PASS — 10 tests |
| `python tools/aisdf_runtime/aisdf.py --help` | PASS |
| JSON manifest parse | PASS |
| MK Framework infographic exists | PASS |

## Scope of validation

These checks validate repository structure, documented contracts, existing automated tests, and CLI startup. They do not certify market outcomes, live AI-provider adapters, autonomous orchestration, or production deployments.
