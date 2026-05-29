# Codex Plugin Spec In This Repo

This repository now keeps a Codex-compatible plugin manifest alongside the existing Claude-oriented files.

## Required layout

Every plugin under `plugins/<plugin-name>/` should include:

```text
plugins/<plugin-name>/
├── .codex-plugin/
│   └── plugin.json
├── .claude-plugin/
│   └── plugin.json
├── commands/
├── agents/              # optional
└── README.md
```

`/.codex-plugin/plugin.json` is the required Codex manifest.
`/.claude-plugin/plugin.json` is currently kept for backward compatibility with the existing command packaging flow in this repository.

## Codex manifest rules

`plugins/<plugin-name>/.codex-plugin/plugin.json` must:

- use the normalized plugin directory name as `name`
- include strict semver in `version`
- include non-empty `description`
- include `author.name`
- include an `interface` object with:
  - `displayName`
  - `shortDescription`
  - `longDescription`
  - `developerName`
  - `category`
  - `capabilities` as a string array
  - `defaultPrompt` or `default_prompt`

Unsupported fields should not be added unless the plugin actually includes the companion files:

- `skills` only when a `skills/` directory exists
- `apps` only when `.app.json` exists
- `mcpServers` only when `.mcp.json` exists

This repository intentionally does not put `commands` or `agents` into the Codex manifest because the current validator only accepts the Codex ingestion contract fields.

## Marketplace rules

The repository marketplace file is:

`./.agents/plugins/marketplace.json`

Each plugin entry should use:

- `source.source = "local"`
- `source.path = "./plugins/<plugin-name>"`
- `policy.installation = "AVAILABLE"`
- `policy.authentication = "ON_INSTALL"`
- a non-empty `category`

## Validation

Use the bundled plugin-creator validator:

```bash
python3 /Users/luoyi/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py plugins/branch-commands
```

Run it once per plugin root. A plugin passes when `/.codex-plugin/plugin.json` exists and all required fields match the Codex validator.
