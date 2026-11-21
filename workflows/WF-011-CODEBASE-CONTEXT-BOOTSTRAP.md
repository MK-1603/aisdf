# WF-011 — Codebase Context Bootstrap

**Purpose:** Build a navigable, evidence-backed map of an existing repository for future engineering work.

## Procedure
1. Confirm repository root, branch/commit, generated/vendor/secret exclusions and read permissions.
2. Inventory the tree without dumping sensitive content. Identify packages, services, entry points, build/test/deploy configuration, schemas, API contracts and ownership metadata.
3. Generate directory-level summaries bottom-up: leaf directories first, then parent directories, then repository root.
4. Each statement must be grounded in file paths, symbols or configuration. Distinguish observed behavior from inferred purpose.
5. Link important architecture, dataflow, dependencies, runtime boundaries and test/deployment entry points.
6. Flag unknowns, stale docs, dead paths and contradictory descriptions rather than inventing explanations.
7. Human owner reviews generated maps before they become canonical project knowledge.
8. Register approved outputs with AKIS/persistent memory using source revision, provenance, freshness and supersession metadata.

## Safety
Exclude secrets, credentials, personal data, generated artifacts and vendored content unless explicitly required and authorized. Do not modify source code. Generated documentation is untrusted until reviewed.

## Outputs
Repository map, directory summaries, architecture index, unknowns register and review record.
