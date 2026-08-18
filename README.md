# CollabCraft Plugins

A repository of team knowledge and deterministic workflow plugins for Claude
Code. Native model capabilities handle routine operations; plugins supply team
conventions and valuable multi-system workflows.

## Plugins

| Plugin | Commands | Description |
|--------|----------|-------------|
| **git-workflow** | `/commit-push-mr` + automatic skill | Team Git conventions and GitLab delivery |
| **gitlab-mr** | `/mr-beautify`, `/mr-list`, `/mr-update` | GitLab MR workflow |
| **dependency-upgrade** | `/turtle-upgrade` | Dependency upgrade workflow |
| **plugin-linter** | `/plugin-lint` | Plugin convention checks |

## Layout

Each plugin follows the Claude Code plugin structure:

```text
plugins/<plugin-name>/
├── .claude-plugin/
│   └── plugin.json
├── skills/              # optional team knowledge and decision rules
├── commands/            # optional explicit workflow entry points
├── agents/              # optional reusable specialist context
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
/plugin install git-workflow gitlab-mr dependency-upgrade@collabcraft-plugins
```

## Reference

- Plugin inventory: [`plugins/README.md`](./plugins/README.md)
