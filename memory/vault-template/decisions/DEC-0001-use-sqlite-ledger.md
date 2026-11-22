---
id: DEC-0001
title: Use a hash-chained SQLite ledger for audit events
memory_type: decision
status: CURRENT
classification: internal
recorded_at: 2026-11-22
authority: verified
project_id: DEMO
workspace_id: local
source_refs:
  - runtime/aisdf_runtime/workforce.py
---
Decision: audit events are stored in SQLite with a hash chain so edits are detectable (verify-ledger). Tamper-evident, not tamper-proof.
