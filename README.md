# CollabCraft Plugins

A collection of team Git workflow plugins for Claude Code.

## Plugins

| Plugin | Commands | Description |
|--------|----------|-------------|
| **branch-commands** | `/branch-create`, `/branch-switch`, `/branch-delete` | Git branch workflow |
| **commit-commands** | `/commit`, `/commit-push`, `/commit-push-mr` | Git commit workflow |
| **mr-commands** | `/mr-beautify`, `/mr-list` | GitLab MR workflow |
| **deploy-commands** | `/build`, `/publish`, `/release` | Build & publish workflow |
| **upgrade-commands** | `/turtle-upgrade` | Dependency upgrade workflow |

## Installation

```bash
/plugin marketplace add ./collabcraft-plugins
/plugin install branch-commands commit-commands mr-commands deploy-commands upgrade-commands@collabcraft-plugins
```

Or browse in `/plugin > Discover`.

## Plugin Structure

Each plugin follows the standard structure:

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json      # Plugin metadata (required)
├── commands/            # Slash commands
└── README.md            # Documentation
```
