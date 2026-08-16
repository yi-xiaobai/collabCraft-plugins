# Git Workflow

Team-specific Git conventions for Claude Code.

The `git-workflow` skill is applied automatically when Claude creates branches,
commits changes, pushes work, handles pre-commit failures, or prepares GitLab
merge requests. Ordinary Git operations use Claude's native capabilities rather
than dedicated command wrappers.

## Team conventions

- Versioned branch names: `{type}_{slug}_v{N}`
- Conventional Commits
- Safe handling of dirty worktrees, secrets, hooks, and force pushes
- GitLab merge requests targeting `dev` by default
- Squash merge and source branch removal

## Command

### `/commit-push-mr`

Keeps one explicit entry point for the multi-step GitLab delivery workflow:

```text
/commit-push-mr
/commit-push-mr to main
/commit-push-mr draft to dev
```

Branch creation, switching, merging, committing, and pushing do not need slash
commands. Ask Claude in natural language; the skill supplies the team rules.
