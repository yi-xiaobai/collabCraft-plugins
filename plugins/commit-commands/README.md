# Commit Commands

Git commit workflow commands: commit, push, create MR.

All commands delegate Conventional Commits message generation to the
[`commit-message-writer`](./agents/commit-message-writer.md) subagent, so the
commit format stays consistent across the whole plugin.

## Commands

### /commit

Stages changes and creates a git commit with an auto-generated message.

### /commit-push

Stages, commits, and pushes to remote in one step.

### /commit-push-mr

```bash
/commit-push-mr [target_branch] [--wip]
```

Stages, commits, pushes, and creates a GitLab MR. Default target: `dev`.

## Agents

### commit-message-writer

Reads the staged diff and returns a Conventional Commits message. Used by all
three commands above. See [`agents/commit-message-writer.md`](./agents/commit-message-writer.md).

## Requirements

- Git 2.x+
- `glab` CLI (for `/commit-push-mr`)
