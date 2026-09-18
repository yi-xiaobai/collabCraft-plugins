# Plugin Linter

Checks Claude Code commands, agents, skills, manifests, Marketplace entries,
and README command references for repository conventions.

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
- **Repository**: Claude/Codex manifests, both Marketplace inventories, plugin
  names, versions, Skill paths, and documented commands

The implementation uses Python rather than GNU-specific `grep` features, so
the same validation runs on macOS and Linux.

## Reference

[Official spec](https://github.com/anthropics/claude-plugins-official)
