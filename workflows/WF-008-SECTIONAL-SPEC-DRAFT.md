# WF-008 — Section-by-Section Specification Drafting

**Purpose:** Convert an approved concept brief into a complete, reviewable technical design without prematurely implementing it.

## Procedure
1. Ingest the approved concept brief, project baseline, source evidence and relevant decisions; confirm the correct project/revision with the human.
2. Draft the design using `standards/DESIGN-SPECIFICATION-STANDARD.md` and `templates/DESIGN-SPECIFICATION.template.md`.
3. Work section by section. After each material section, write the artifact, summarize changes and request approve/revise feedback. Preserve inline comments and accepted decisions.
4. For architecture/data/security/hosting choices with multiple defensible options, present options with mechanism, trade-offs, cost and failure conditions. Human owner selects.
5. Separate feature-level architecture from detailed implementation plan.
6. Include exact target file create/modify/delete allowlist, test plan, migration and rollback plan.
7. Run completeness checks and validate links, schema references and requirement traceability.
8. Mark `IN_REVIEW` only after required sections are present and the owner authorizes review.

## Write boundary
During this workflow, write only approved specification artifacts, concept notes and review-support files. Do not modify production source, dependencies, lockfiles, migrations or deployment configuration.

## Outputs
Versioned design specification, decision log, traceability matrix, file allowlist and test plan.
