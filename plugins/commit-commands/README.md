# Commit Commands

Git commit workflow commands: commit, push, create MR, and undo.

## Commands

### /commit

Auto-generates and creates a git commit.

### /commit-push

Commits and pushes to remote in one step.

### /commit-push-mr

```bash
/commit-push-mr [target_branch]
```

Commits, pushes, and creates a GitLab MR. Default target: `dev`.

### /commit-undo

```bash
/commit-undo [mode]
```

Undoes the last commit while preserving changes.

| Mode | Behavior |
|------|----------|
| `soft` (default) | Keep changes staged |
| `mixed` | Keep changes unstaged |
| `hard` | Discard all changes |

## Requirements

- Git 2.x+
- `glab` CLI (for `/commit-push-mr`)
