---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git diff:*), Bash(git push:*), Bash(git fetch:*), Bash(git pull:*), Bash(git branch:*)
description: Commit and push to remote
---

## Context

- Current git status: !`git status`
- Current git diff (staged and unstaged changes): !`git diff HEAD`
- Current branch: !`git branch --show-current`
- Recent commits: !`git log --oneline -5`

## Your task

Based on the above changes, commit and push to remote.

1. Analyze the changes and generate a commit message using Conventional Commits format:
   - `feat`: New feature
   - `fix`: Bug fix
   - `docs`: Documentation
   - `style`: Code style
   - `refactor`: Refactoring
   - `chore`: Build/tools

2. Stage relevant files (avoid .env, credentials, secrets)

3. Create the commit

4. Push to remote origin

## Error Handling

- **禁止使用 `--no-verify`、`--force` 等绕过检查的参数**
- 如果 pre-commit 检查失败：
  - **样式问题**（如 lint、格式化错误）：pre-commit 会自动修复，重新 stage 修改后的文件并再次提交即可
  - **逻辑问题**（如分支命名不规范、代码逻辑错误）：立即终止流程，向用户报告失败原因
- 其他步骤失败（如 push）：立即终止流程，向用户报告失败原因

You have the capability to call multiple tools in a single response. Stage, commit, and push in a single message. Do not use any other tools or do anything else. Do not send any other text or messages besides these tool calls.
