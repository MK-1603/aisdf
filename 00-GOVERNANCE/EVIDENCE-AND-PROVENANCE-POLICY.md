# Evidence and Provenance Policy

Evidence must be attributable, relevant, dated where time matters, and sufficient for the claim. Record artifact/source, exact version or commit where applicable, retrieval/execution date, method, owner, result and limitations.

Evidence classes: PRIMARY_SOURCE, EXECUTION_LOG, TEST_RESULT, REVIEW_RECORD, OBSERVATION, SECONDARY_SOURCE, USER_ASSERTION. Distinguish source-backed facts from assumptions and model-generated suggestions. Screenshots alone are weak evidence for hidden system state; pair them with logs, commands or reproducible checks where possible.

Never fabricate citations, test output, tool runs, approval, commits or deployment state. Redact secrets and personal data. Preserve failed and skipped results, not only passing evidence.

## Additional detail (carried from the starter seed)
## Provenance classes
`USER_PROVIDED`, `REPOSITORY_OBSERVED`, `OFFICIALLY_VERIFIED`, `INDEPENDENTLY_CORROBORATED`, `MODEL_KNOWLEDGE`, `INFERENCE`, `ASSUMPTION`, `RECOMMENDATION`, `UNKNOWN`.

Do not convert an assumption or inference into a fact through repetition.

## Evidence record
Each evidence item identifies evidence ID, claim/requirement, source artifact, exact revision, collection method, timestamp, actor/tool, environment, result, limitations and reviewer where applicable.

## Evidence quality
- Direct execution output is stronger than an assertion.
- Reproducible commands and test reports are preferred.
- Screenshots may support visual review but do not replace source/test evidence.
- Search snippets are not authoritative evidence for consequential decisions.
- Evidence must match the code/document revision being evaluated.

## Privacy
Do not record secrets or unnecessary personal data. Redact sensitive output while preserving verifiability.
