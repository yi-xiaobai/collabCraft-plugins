---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git diff:*)
description: Create a git commit with auto-generated message
---

## Context

- Current git status: !`git status`
- Current git diff (staged and unstaged changes): !`git diff HEAD`
- Current branch: !`git branch --show-current`
- Recent commits: !`git log --oneline -10`

## Your task

Based on the above changes, create a single git commit.

1. Stage relevant files (avoid `.env`, credentials, secrets)
2. **Delegate message generation to the `commit-message-writer` subagent**
   - The subagent reads the staged diff and returns a Conventional Commits message
   - Do NOT inline message rules here — trust the subagent's output
3. Create the commit with the returned message

You MUST do all of the above in a single message.
