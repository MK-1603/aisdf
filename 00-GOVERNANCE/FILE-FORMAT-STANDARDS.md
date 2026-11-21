# AISDF File Format Standards

**Status:** PROPOSED

| Format | Canonical use | Rule |
|---|---|---|
| `.md` | Human-readable documentation, rules, workflows, prompts | Primary documentation format |
| `.json` | Schemas, structured records, registries and fixtures | Validate syntax and schema conformance |
| `.yaml` / `.yml` | Configuration and project/work-unit templates | Validate structure; avoid duplicate JSON/YAML sources |
| `.py` | Repository validation and automation | Include tests and safe failure behavior |
| `.sh` / `.ps1` | POSIX shell / PowerShell automation | State platform assumptions |
| `.toml` | Tool and project configuration | Follow the consuming tool specification |
| `.csv` | Tabular exports and benchmark data | Include headers and document units |
| `.svg` / `.png` | Diagrams and visual assets | Keep editable source where practical |
| `.pdf` | Distribution snapshots | Generated from canonical source; not primary editable source |

Use the simplest format that fits the consumer. Markdown is not a substitute for structured data, and a PDF should not become the only editable copy of framework documentation.
