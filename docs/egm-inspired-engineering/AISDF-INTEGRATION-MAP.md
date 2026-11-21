# AISDF Integration Map — EGM-Inspired Extension

| Extension artifact | Proposed AISDF home | Reused existing capabilities |
|---|---|---|
| WF-007 Concept Challenge | `workflows/` | E-003 problem discovery, E-009 risk/premortem, E-010 scope/kill criteria |
| WF-008 Spec Draft | `workflows/` | E-012 requirements, E-014 product specification, E-025 architecture, E-015 acceptance criteria |
| WF-009 Independent Design Review | `workflows/` | E-030 architecture change control, E-042 approval, E-045 code review, E-046 security, E-043 test strategy |
| WF-010 Finding Resolution | `workflows/` | E-030, E-038, E-042, E-045 |
| WF-011 Codebase Bootstrap | `workflows/` | E-004 existing-project X-Ray, E-031 AKIS, E-040 project state |
| WF-012 Specification Drift | `workflows/` | E-030, E-040, E-045, E-054 observability |
| Design standard | `00-GOVERNANCE/` or design standards | documentation, evidence, schema and workflow standards |
| Reviewer personas | `prompts/roles/` or `personas/` | existing analyst, architect, test, security and code-review roles |
| Finding schema | `schemas/` | source evidence, rule-check, work-unit and completion-report schemas |

## Integration rule

This map is a proposed additive integration. It does not change the canonical core engine registry or assert that these workflows are installed in the live GitHub repository. When integrating into the canonical repository, reconcile filenames, version, schema IDs, links and governance approval first.
