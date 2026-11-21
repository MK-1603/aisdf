# AISDF Persistent Memory Architecture

## 1. Purpose
Provide durable, portable project and agent memory across sessions and tools without replacing AISDF knowledge intelligence or canonical project-state records.

## 2. Relationship to existing AISDF
| Capability | Owns | Memory relationship |
|---|---|---|
| AKIS E-031 | Knowledge organization, retrieval, ranking, freshness | Retrieves governed memory as a knowledge source |
| E-038 Context & Handoff | Context packaging and ownership transfer | Uses session context packs and handoff references |
| E-040 Project State & Continuity | Canonical project state | Remains authoritative; memory provides compact recall views |
| `knowledge-entry.schema.json` | General knowledge metadata | Continues for knowledge; memory schema adds lifecycle/scope metadata |

**Boundary:** AKIS answers how knowledge is organized and retrieved. Persistent Memory defines what survives sessions, how it is versioned, and how it is safely recalled.

## 3. Logical architecture
```text
Approved sources / session outcomes / handoffs
                    |
          Capture & classification
                    |
      Provenance + consent + validation
                    |
             Canonical memory
       /          |          |          \
   Project     Decisions   Sessions   Knowledge refs
                    |
           Rebuildable index
                    |
       AKIS retrieval + freshness
                    |
         Bounded context pack
                    |
          Agent / IDE / workflow
                    |
       Checkpoint / correction /
             supersession
```

## 4. Memory scopes
- **Project:** verified facts, architecture, constraints, accepted decisions, current status.
- **Decision:** decision, rationale, alternatives, approver, date, reconsideration conditions.
- **Session:** task progress, files touched, actual commands/tests, blockers, next action; transient until consolidated.
- **Reusable knowledge:** validated cross-project patterns and runbooks.
- **Preference:** explicitly approved working preferences, scoped to the correct user/workspace.

Keep personal and organizational scopes separate. Cross-project reuse requires authorization and removal of confidential project details.

## 5. Suggested portable layout
```text
.memory/
  README.md
  INDEX.md
  projects/<project-id>/
    PROJECT-MEMORY.md
    DECISIONS/
    SESSIONS/
    HANDOFFS/
    KNOWLEDGE/
  audit/
  schemas/
```
Path is configurable. Do not assume memory should be committed to Git. Define ignore, encryption, backup and access policies per project. Obsidian may be an optional UI over Markdown files.

## 6. Lifecycle
Capture → classify → validate → approve where required → persist → index → retrieve → verify freshness → use → checkpoint → reconcile/supersede → review/expire.

Indexes, embeddings and graph views are derived data and must be rebuildable.

## 7. Bounded retrieval
Filter by project/workspace and access first; prefer exact IDs and file references; rank by relevance, authority, confidence and freshness; cap context; deduplicate; return source paths/status; abstain when evidence is inadequate. Never inject an entire vault into every prompt.

## 8. Consistency
Use atomic writes where supported; detect revision conflicts; preserve user-authored sections; separate generated and human-owned content; report index failures separately from canonical save failures; never silently merge conflicting decisions.

## 9. Adapter boundary
Possible adapters: Markdown/Obsidian, Git-backed Markdown, SQLite/FTS, optional vector index, MCP, CLI and IDE/agent hooks. None is certified until permission boundaries, data flow, concurrency, recovery and conformance tests pass.

## 10. Non-goals
Not an autonomous agent, Git replacement, secrets manager, universal personal-data store, or guarantee of perfect recall.
