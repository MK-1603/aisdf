# Schema Standards

- Use JSON Schema Draft 2020-12 and declare `$schema` and a stable `$id` where practical.
- Define required fields, types, enums, bounds, formats and `additionalProperties` policy.
- Provide valid and invalid fixtures.
- Test schema validity and instance conformance in CI.
- Treat breaking schema changes as versioned migrations.
- Do not place secrets or real personal data in fixtures.
