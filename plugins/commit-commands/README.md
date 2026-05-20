# Commit Commands

Git commit workflow commands: commit, push, create MR.

All commands delegate Conventional Commits message generation to the
[`commit-message-writer`](./agents/commit-message-writer.md) subagent, so the
commit format stays consistent across the whole plugin.

Pre-commit hook recovery is centralized in the
[`pre-commit-handler`](./agents/pre-commit-handler.md) subagent. Other plugins
that create git commits (e.g. `branch-merge`, `publish`, `turtle-upgrade`) also
delegate to it.

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

### pre-commit-handler

Recovers from pre-commit hook failures: auto-fixes **real source code/style**
violations and returns `RETRY`. For hook infrastructure, check
baseline/threshold/limit data, or metric budget exceeded, returns `STOP` so the
user resolves manually — never auto-bumps baselines or thresholds. Shared
across commit, branch, deploy, and upgrade workflows. See
[`agents/pre-commit-handler.md`](./agents/pre-commit-handler.md).

## Requirements

- Git 2.x+
- `glab` CLI (for `/commit-push-mr`)
