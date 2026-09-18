# CollabCraft Plugins

A repository of team knowledge and deterministic workflow plugins for Claude
Code and Codex. Native model capabilities handle routine operations; plugins
supply team conventions and valuable multi-system workflows.

## Plugins

| Plugin | Commands | Description |
|--------|----------|-------------|
| **git-workflow** | `/commit-push-mr` + automatic skill | Team Git conventions and GitLab delivery |
| **gitlab-mr** | `/mr-beautify`, `/mr-list`, `/mr-update` | GitLab MR workflow |
| **dependency-upgrade** | `/turtle-upgrade` | Dependency upgrade workflow |
| **plugin-linter** | `/plugin-lint` | Plugin convention checks |
| **weekly-report** | `/weekly-report` + automatic skill | Weekly work summaries from Git commits |

## Layout

Each plugin shares one capability implementation across Claude Code and Codex:

```text
plugins/<plugin-name>/
├── .claude-plugin/
│   └── plugin.json
├── .codex-plugin/
│   └── plugin.json
├── skills/              # optional team knowledge and decision rules
├── commands/            # optional explicit workflow entry points
├── agents/              # optional reusable specialist context
└── README.md
```

The repository marketplace files are:

```text
.claude-plugin/marketplace.json
.agents/plugins/marketplace.json
```

## Claude Code installation

Add the repository marketplace and then install plugins from it:

```bash
/plugin marketplace add ./.claude-plugin
/plugin install git-workflow@collabcraft-plugins
/plugin install gitlab-mr@collabcraft-plugins
/plugin install dependency-upgrade@collabcraft-plugins
/plugin install weekly-report@collabcraft-plugins
/plugin install plugin-linter@collabcraft-plugins
```

## Codex installation

Add the repository-local marketplace, then install the required plugins:

```bash
codex plugin marketplace add ./.agents/plugins
codex plugin add git-workflow@collabcraft-plugins
codex plugin add gitlab-mr@collabcraft-plugins
codex plugin add dependency-upgrade@collabcraft-plugins
codex plugin add weekly-report@collabcraft-plugins
codex plugin add plugin-linter@collabcraft-plugins
```

Claude slash commands remain explicit entry points. Codex discovers the same
workflow rules through each plugin's Skill.

## Reference

- Plugin inventory: [`plugins/README.md`](./plugins/README.md)
