# AISDF Workflow Runtime

The portable WF-007–WF-012 CLI is implemented in `../aisdf_runtime/aisdf.py`. Run it from the repository root:

```bash
python tools/aisdf_runtime/aisdf.py --help
python tools/aisdf_runtime/aisdf.py init --project /path/to/your/project
```

It creates `.aisdf/` project artifacts and does not edit application source files. See `docs/WORKFLOW-RUNTIME.md` for commands and limits.
