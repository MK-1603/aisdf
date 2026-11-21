# AISDF Tools

- `validate_repository.py` validates repository structure, internal Markdown links, JSON schemas and fixtures.
- `aisdf_runtime/aisdf.py` provides the WF-007–WF-012 artifact workflow CLI.
- `aisdf_runtime/project.py` provides WF-013 project definition, deterministic inventory, plan scaffolding, approval digest, and gated prompt generation.

The tools do not invoke model APIs, spawn agents, edit target application source, or grant permissions. AI reasoning and real implementation occur in the connected host environment under human-approved scope.
