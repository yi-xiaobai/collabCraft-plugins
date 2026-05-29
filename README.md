# CollabCraft Plugins

A repository of team Git workflow plugins with Codex-compatible manifests.

## Plugins

| Plugin | Commands | Description |
|--------|----------|-------------|
| **branch-commands** | `/branch-create`, `/branch-switch`, `/branch-merge` | Git branch workflow |
| **commit-commands** | `/commit`, `/commit-push`, `/commit-push-mr` | Git commit workflow |
| **mr-commands** | `/mr-beautify`, `/mr-list`, `/mr-update` | GitLab MR workflow |
| **deploy-commands** | `/build`, `/publish`, `/release` | Build and publish workflow |
| **upgrade-commands** | `/turtle-upgrade` | Dependency upgrade workflow |
| **plugin-linter** | `/plugin-lint` | Plugin convention checks |

## Codex Layout

Each plugin now keeps a Codex manifest in addition to the existing Claude-oriented files:

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

The repository marketplace file for Codex is:

```text
.agents/plugins/marketplace.json
```

## Installation

If your Codex setup supports repo-local marketplaces, add the repository marketplace and then install plugins from it:

```bash
codex plugin marketplace add ./.agents/plugins
codex plugin install branch-commands commit-commands mr-commands deploy-commands upgrade-commands plugin-linter@collabcraft-plugins
```

## Reference

- Codex repository-specific notes: [`docs/codex-plugin-spec.md`](./docs/codex-plugin-spec.md)
- Plugin inventory: [`plugins/README.md`](./plugins/README.md)
