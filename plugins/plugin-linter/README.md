# Plugin Linter

Checks Claude Code plugins for compliance with official spec.

## Commands

| Command | Description |
|---------|-------------|
| `/plugin-lint` | Check all plugin files |
| `/plugin-lint path/to/file.md` | Check a single file |

## Checks

- **YAML Front Matter**: `allowed-tools` must specify exact command patterns; `description` must be present and concise
- **Structure**: must have `## Context` and `## Your task` sections
- **Your task**: no hardcoded scripts; describes *what* not *how*; must include a single-response instruction

## Reference

[Official spec](https://github.com/anthropics/claude-plugins-official)
