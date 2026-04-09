# CLAUDE.md

CollabCraft Plugins - Team Git Workflow Plugin Collection

All responses and files in English.

```
plugins/
  ├── branch-commands/      # Git branch workflow
  ├── commit-commands/      # Git commit workflow
  ├── mr-commands/          # GitLab MR workflow
  ├── deploy-commands/      # Build and deployment workflow
  ├── upgrade-commands/     # Dependency upgrade workflow
  └── plugin-linter/        # Plugin compliance checker
docs/                       # Design documents
scripts/lint-plugins.sh     # Plugin lint script
```

Each plugin: `.claude-plugin/plugin.json` + `commands/*.md` + `README.md`.

Run `bash scripts/lint-plugins.sh` after commit or push — must pass.

`allowed-tools` use exact patterns like `Bash(git:*)`, never generic `Bash`.

Commit format: `type(scope): message`
