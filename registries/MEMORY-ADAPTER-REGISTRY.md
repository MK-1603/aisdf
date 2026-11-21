# Memory Adapter Registry

**Status:** capability categories only; no adapter is certified here.

| Adapter | Role | Required verification |
|---|---|---|
| Markdown / Obsidian | Human-readable canonical notes and graph | Scoped paths, metadata preservation, atomic writes, conflicts, access, backup/restore |
| Git-backed Markdown | Versioned/reviewable team memory | Commit permissions, merge conflicts, secret scanning, private-data exclusion |
| SQLite / FTS | Local structured storage and lexical retrieval | Migrations, transactions, backup, query isolation |
| Vector index | Optional semantic recall | Rebuildability, data egress, tenant isolation, deletion propagation, stale-index detection |
| MCP | Agent-neutral interface | Tool allowlist, caller identity, scoped paths, read/write separation, audit |
| IDE/agent hooks | Context loading and checkpoint capture | Opt-in, bounded injection, fail-closed behavior, no privilege expansion |

Record adapter name/version/source/license, supported operations, permissions, data flow, limitations, test evidence and status. Status: `PROPOSED`, `IN_EVALUATION`, `NOT_VERIFIED`, `VERIFIED_LIMITED`, `DEPRECATED`. README claims alone do not establish verification.

Obsidian is optional. AISDF memory must remain usable without it.
