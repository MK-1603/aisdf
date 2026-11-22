# Tool Compatibility Matrix

AISDF is tool-independent by design: the shared contract is Markdown (`AGENTS.md`, `PROJECT.md`) plus the optional local runtime CLI (`python aisdf.py`). **"Works with any tool" is not claimed. Each row must be earned by a recorded conformance run** (`adapters/CONFORMANCE.md`).

Integration levels: **I0** none/untested - **I1** rules file only (the tool can read AGENTS.md/PROJECT.md) - **I2** assisted handoff (a human carries context and results) - **I3** tool runs `python aisdf.py` commands under human approval - **I4** native adapter implementing `runtime/adapters/WORKER-ADAPTER-CONTRACT.md` with recorded evidence.

| Tool | Level claimed today | Conformance run recorded | Notes |
|---|---|---|---|
| Any CLI/IDE agent that reads `AGENTS.md` | I1 (untested) | none | Entry prompt is plain Markdown. Verify the tool actually loads the file |
| Claude Code | I1 (untested) | none | Use `CLAUDE.md` pointing at `AGENTS.md`; I3 is possible because it can run shell commands under approval |
| Cursor / Antigravity / Codex / OpenCode | I1 (untested) | none | Templates under `adapters/` where present; confirm each tool's current rules-file name |
| Kimi Code, Qwen Code | I0 | none | Not verified. Try `AGENTS.md`; record the result before claiming anything |
| ChatGPT / other chat UIs | I2 | none | Cannot run local commands; paste `MASTER-ENTRY-PROMPT.md` and carry evidence by hand |

Rows move up only when `adapters/CONFORMANCE.md` has been run and the result is committed under `adapters/conformance-results/`.
