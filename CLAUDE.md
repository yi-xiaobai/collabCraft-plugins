# CLAUDE.md

CollabCraft Plugins - Team Git Workflow Plugin Collection

All responses and files in English.

```
plugins/
  ├── git-workflow/         # Team Git skill + GitLab delivery command
  ├── mr-commands/          # GitLab MR workflow
  ├── upgrade-commands/     # Dependency upgrade workflow
  └── plugin-linter/        # Plugin compliance checker
docs/                       # Design documents
scripts/lint-plugins.sh     # Plugin lint script
```

Each plugin: `.claude-plugin/plugin.json` + at least one capability directory + `README.md`.

- `skills/*/SKILL.md` — team knowledge and decision rules loaded when relevant
- `commands/*.md` — explicit entry points for valuable multi-step workflows
- `agents/*.md` — reusable specialists shared by multiple workflows

Run `bash scripts/lint-plugins.sh` after commit or push — must pass.

`allowed-tools` use exact patterns like `Bash(git:*)`, never generic `Bash`.

Commit format: `type(scope): message`

## Design Principle

Use native model capabilities for general-purpose operations. Package stable team
knowledge and judgment as skills, deterministic enforcement as scripts/hooks/CI,
and explicit commands only for valuable multi-step or cross-system workflows.

Do not create a subagent for logic used by only one command.
