# Knowledge Metadata Standard

Every reusable knowledge entry should record: `id`, `title`, `domain`, `summary`, `content`, `source_evidence[]`, `technology[]`, `version_scope`, `status`, `confidence`, `created_at`, `verified_at`, `review_due_at`, `owner`, `related_entries[]`, `limitations` and `change_history[]`. Use the knowledge-entry schema. Missing dates must be null/unknown, not guessed.

## Additional detail (carried from the starter seed)
Every canonical knowledge document should begin with YAML front matter:

```yaml
---
id: KNOW-EXAMPLE-001
title: Example knowledge topic
status: draft
version: 1.0.0
owner: maintainers
knowledge_type: engineering-guidance
source_class: official
source_url: https://example.invalid/
source_version: unknown
verified_at: null
next_review_due: null
confidence: unverified
tags: []
supersedes: []
superseded_by: []
---
```

Do not use placeholder URLs in published verified knowledge. Use `null` or `unknown` when data is unavailable. Keep canonical content in Markdown and register it by stable ID.
