# Technology Support and Deprecation Policy

Classify each dependency/tool as ACTIVE, MAINTENANCE, LIMITED, DEPRECATED or UNSUPPORTED. Track vendor support dates, security updates, migration path, owner and review date. New adoption of deprecated/unsupported technology requires explicit risk acceptance and migration plan. Deprecation decisions must identify affected projects, replacement options, breaking changes and rollback constraints.

## Additional detail (carried from the starter seed)
Classify dependencies as `CURRENT`, `MAINTENANCE`, `DEPRECATED`, `END_OF_LIFE` or `UNKNOWN`.

Before adoption or upgrade:
1. Check official lifecycle/support documentation.
2. Check release notes and breaking changes.
3. Check security advisories and known vulnerabilities.
4. Verify compatibility with project runtime and dependencies.
5. Record migration and rollback strategy.

When a dependency is deprecated or end-of-life, assess exposure, replacement options, migration cost and deadline. Do not upgrade blindly; use a tested migration plan and approval where behavior/data may change.
