# Adapter Freshness Register

Maintain one record per adapter/tool integration: adapter ID, target product, supported versions/plans, contract version, verified capabilities, last test, test environment, known failures, owner, status and next review. Re-test after breaking API/UI changes, provider release changes or reported failures. If no recent verification exists, mark NOT_VERIFIED rather than silently assuming compatibility.
