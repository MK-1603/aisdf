# Adapter Freshness Register

Maintain one record per adapter/tool integration: adapter ID, target product, supported versions/plans, contract version, verified capabilities, last test, test environment, known failures, owner, status and next review. Re-test after breaking API/UI changes, provider release changes or reported failures. If no recent verification exists, mark NOT_VERIFIED rather than silently assuming compatibility.

## Additional detail (carried from the starter seed)
Maintain one entry per adapter:
- Adapter ID/name and target product.
- Official product/documentation reference.
- Adapter specification version.
- Tested product version and plan where applicable.
- Last verification date and method.
- Verified capabilities and limitations.
- Permission/data boundaries.
- Status and next review date.
- Known breaking changes and supersession reference.

Do not mark an adapter verified without a reproducible test. If a product changes or review is overdue, downgrade to `NOT_VERIFIED` until rechecked.
