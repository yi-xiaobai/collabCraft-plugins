# Plugin Linter

Checks Claude Code commands, agents, and skills for repository conventions.

## Commands

| Command | Description |
|---------|-------------|
| `/plugin-lint` | Check all plugin files |
| `/plugin-lint path/to/file.md` | Check a single file |

## Checks

- **YAML Front Matter**: `allowed-tools` must specify exact command patterns; `description` must be present and concise
- **Commands**: context, task, tool scope, and sequential execution
- **Agents**: reusable role, name, description, and tool scope
- **Skills**: matching name, trigger description, language, and team-specific scope

## Reference

[Official spec](https://github.com/anthropics/claude-plugins-official)
