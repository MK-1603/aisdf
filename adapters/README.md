# AI Tool Adapters

AISDF core is provider-neutral. Each adapter should load the same canonical project contract (`PROJECT.md`) and operating contract (`AGENTS.md`) while using native host discovery files where necessary.

| Environment | Primary instruction entry | Additional adapter | Notes |
|---|---|---|---|
| OpenAI Codex | `AGENTS.md` | `.agents/skills/aisdf/SKILL.md` | Verify loaded instructions in the host session. |
| Claude Code | `CLAUDE.md` | `.claude/skills/aisdf/SKILL.md` | Recommended bridge: `@AGENTS.md`; do not assume fallback behavior across versions. |
| Cursor | `AGENTS.md` | `.cursor/rules/aisdf.mdc` | Keep the `.mdc` frontmatter valid. |
| Google Antigravity | `AGENTS.md` / `GEMINI.md` as supported | `.agents/rules/aisdf.md`, `.agents/skills/aisdf/SKILL.md` | Verify workspace discovery and plugin compatibility in installed version. |

Adapters do not grant permissions or prove host compatibility. Always inspect existing instructions before installing; merge rather than overwrite. See [PROJECT.md and AGENTS.md](../docs/project-lifecycle/PROJECT-AND-AGENT-FILES.md).
