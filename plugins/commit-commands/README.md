# Commit Commands Plugin

Streamline your git workflow with commands for committing, pushing, and creating merge requests.

## Overview

This plugin automates common git operations, reducing context switching and manual command execution. Instead of running multiple git commands, use a single slash command to handle your entire workflow.

## Commands

### /commit

```bash
/commit
```

Creates a git commit with an automatically generated commit message.

### /commit-push

```bash
/commit-push
```

Commits and pushes to remote in one step.

### /commit-push-mr

```bash
/commit-push-mr [target_branch]
```

Commits, pushes, and creates a GitLab MR in one step.

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `target_branch` | 目标分支 | dev |

### /commit-undo

```bash
/commit-undo [mode]
```

Undo the last commit while preserving changes.

| 模式 | 说明 | 变更保留 |
|------|------|----------|
| `soft` | 撤销提交，保留暂存 | ✅ staged |
| `mixed` | 撤销提交，取消暂存 | ✅ unstaged |
| `hard` | 撤销提交，丢弃变更 | ❌ 丢失 |

示例：
```bash
/commit-undo           # 默认 soft 模式
/commit-undo hard      # 丢弃所有变更（需确认）
```

## Installation

```bash
/plugin install commit-commands@team-plugins
```

## Best Practices

### Using /commit

- Review the generated commit message
- Use for quick commits during development

### Using /commit-push

- Use when you're ready to share your work
- Good for feature branches

### Using /commit-push-mr

- Use when feature is complete and ready for review
- Ensures clean MR with squashed commits

## Workflow Integration

### Quick commit workflow

```bash
# Make changes
/commit
```

### Feature branch workflow

```bash
# During development
/commit-push

# When ready for review
/commit-push-mr
```

## Troubleshooting

### /commit creates empty commit

- Check if there are actual changes: `git status`
- Ensure files aren't gitignored

### /commit-push fails

- Check if branch is tracking remote
- Verify push permissions

### /commit-push-mr fails to create MR

- 运行 `glab auth login` 重新认证
- 确保分支已推送到远程

## Requirements

- Git 2.x+
- glab CLI (for /commit-push-mr)

## Author

Your Team

## Version

1.0.0
