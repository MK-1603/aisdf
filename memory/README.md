# AISDF Memory

Memory lets an AI coding tool recall project context between sessions. In AISDF it is **recall, not authority**.

## Rules (checked by `python aisdf.py memory-check --vault <dir>`)
1. **Canonical project state outranks memory.** `PROJECT.md`, approved tasks, the audit ledger and ADRs win every conflict (see `00-GOVERNANCE/RULE-PRECEDENCE-AND-CONFLICT-RESOLUTION.md`).
2. **Every note carries provenance:** `id`, `title`, `memory_type`, `status`, `classification`, `recorded_at`, `authority`, `source_refs`. `authority: verified` or `human_confirmed` requires at least one `source_refs` entry.
3. **Authority levels:** `unverified` (anything an AI wrote), `verified` (backed by tool-generated evidence), `human_confirmed` (a registered approver confirmed it). Memory can never certify that work is complete.
4. **Memory is untrusted data.** A note is never an instruction. `memory-check` warns on notes containing instruction-injection phrases (memory poisoning).
5. **The independent reviewer (EGM Goldfish) never receives memory.** `python aisdf.py review-package` builds the reviewer's input from requirements, approved tasks, evidence and the diff only.
6. **Obsidian is optional.** The vault is plain Markdown + frontmatter; any editor works. Obsidian is a convenient human view (graph, backlinks) and is **not a security boundary**.
7. **Concurrent agents:** do not let several agents write the same vault files. Use one writer at a time (git history is the audit trail) or a database-backed gateway with version checks.

## EGM <-> memory flow
```
Elephant (implementer) <-> vault (recall)           Goldfish (independent reviewer)
        |                                                   ^
        | diff + tool evidence                              | requirements + tasks + diff + evidence ONLY
        +----------------> review-package ------------------+
                                  |
                  findings (JSON, schema-validated) -> human disposition
                                  |
        verified lessons -> new vault notes (authority: verified, with source_refs)
```

## Vault layout
`vault-template/` is a starter: `facts/`, `decisions/`, `lessons/`, `sessions/`. Copy it next to (or inside) your project and open it in Obsidian.
