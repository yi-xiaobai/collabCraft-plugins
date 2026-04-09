# CLAUDE.md

CollabCraft Plugins - Team Git Workflow Plugin Collection

## Project Structure

```
plugins/                    # Plugin directory
  ├── branch-commands/      # Git branch workflow
  ├── commit-commands/      # Git commit workflow
  ├── mr-commands/          # GitLab MR workflow
  ├── deploy-commands/      # Build and deployment workflow
  ├── upgrade-commands/     # Dependency upgrade workflow
  └── plugin-linter/        # Plugin compliance checker
docs/                       # Design documents and analysis
scripts/
  └── lint-plugins.sh       # Plugin lint script
```

## Development Guidelines

### Plugin Change Process

1. Modify the corresponding plugin in `plugins/`
2. `bash scripts/lint-plugins.sh` - Validate compliance (must pass)
3. Update the plugin's own README.md

### Lint Rules

- Command files must be in pure English
- Must include YAML frontmatter
- Must have `description` field
- `allowed-tools` must use exact patterns (e.g., `Bash(git:*)`), avoid generic `Bash`
- Must include `## Task` or `## Your task` section
- Recommended to include `## Context` section and single-message instruction

### Commit Guidelines

Format: `type(scope): message`

```bash
feat(branch-commands): add branch sync command
fix(commit-commands): fix commit message format
chore(lint): update lint rules
```
