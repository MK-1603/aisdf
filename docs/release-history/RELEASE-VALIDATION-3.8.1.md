# AISDF 3.8.1 — Local Release Validation

Date: 2026-11-21

## Executed checks

| Check | Result | Evidence |
|---|---|---|
| `python tools/validate_repository.py` | PASS | 56 engine specs; 9 JSON schemas; 2 fixtures; required docs and internal Markdown links validated |
| `python -m pytest -q` | PASS | 10 tests passed |
| `python tools/aisdf_runtime/aisdf.py --help` | PASS | CLI help command exited successfully |
| `python tools/aisdf_runtime/project.py --help` | PASS | CLI help command exited successfully |
| WF-013 lifecycle test | PASS | Test covers init, deterministic assessment, draft plan, blocked unapproved prompt, plan digest, approved prompt generation |
| Non-overwrite test | PASS | Existing PROJECT.md content preserved when init is attempted |

## Scope of validation

These are local repository and helper-tool checks. They do not prove semantic correctness of an arbitrary target project, successful use inside ChatGPT/Claude/Codex/Cursor/Antigravity, genuine independent reviewer isolation, security certification, deployment, or production behavior.

## Human decisions still required

- Review and approve AISDF's own PROJECT.md.
- Choose a license and configure maintainers/security contact.
- Run a reference target project through WF-013 in a live supported host and capture evidence.
- Certify adapters against exact installed host versions.
