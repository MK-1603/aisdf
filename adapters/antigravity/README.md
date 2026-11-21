# Google Antigravity Adapter

Two supported packaging forms are included:

- `workspace/`: copy `.agents/` into the root of the project opened in Antigravity. It provides an always-on AISDF rule and an on-demand `aisdf` skill.
- `plugin/`: versioned distributable plugin with `.antigravity-plugin/plugin.json`, skills, rules, and custom reviewer agent definitions.

Antigravity uses `.agents/skills/<skill-name>/SKILL.md` for workspace skills and `.agents/rules/*.md` for workspace rules. Plugin component directories remain at the plugin root. See the official [Rules](https://antigravity.google/docs/rules/), [Skills](https://antigravity.google/docs/skills), and [Build plugins](https://antigravity.google/docs/build-plugins/) documentation.

## Install workspace adapter

1. Copy the contents of `workspace/` into the target project root.
2. Open/reload the project in Antigravity.
3. Confirm the AISDF skill is discoverable; invoke `/aisdf` if manual invocation is supported by the installed version.
4. Ask the agent to explain the AISDF operating modes and show the files it read before making changes.

## Plugin

Run `agy plugin validate <path-to-plugin>` with a compatible Antigravity CLI before installing. This repository package has not run that host-specific command; plugin validation is therefore pending.
