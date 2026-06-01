# CollabCraft Plugins

A repository of team Git workflow plugins for Claude Code.

## Plugins

| Plugin | Commands | Description |
|--------|----------|-------------|
| **branch-commands** | `/branch-create`, `/branch-switch`, `/branch-merge` | Git branch workflow |
| **commit-commands** | `/commit`, `/commit-push`, `/commit-push-mr` | Git commit workflow |
| **mr-commands** | `/mr-beautify`, `/mr-list`, `/mr-update` | GitLab MR workflow |
| **deploy-commands** | `/build`, `/publish`, `/release` | Build and publish workflow |
| **upgrade-commands** | `/turtle-upgrade` | Dependency upgrade workflow |
| **plugin-linter** | `/plugin-lint` | Plugin convention checks |

## Layout

Each plugin follows the Claude Code plugin structure:

```text
plugins/<plugin-name>/
├── .claude-plugin/
│   └── plugin.json
├── commands/
├── agents/              # optional
└── README.md
```

The repository marketplace file is:

```text
.claude-plugin/marketplace.json
```

## Installation

Add the repository marketplace and then install plugins from it:

```bash
/plugin marketplace add ./.claude-plugin
/plugin install branch-commands commit-commands mr-commands deploy-commands upgrade-commands plugin-linter@collabcraft-plugins
```

## Reference

- Plugin inventory: [`plugins/README.md`](./plugins/README.md)
