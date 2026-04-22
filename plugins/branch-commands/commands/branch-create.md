---
allowed-tools: Bash(git fetch:*), Bash(git branch:*), Bash(git push:*), Bash(git checkout:*), Bash(open:*), Bash(code:*), Bash(windsurf:*)
description: Create a new Git branch with auto-versioning
---

## Context

- Current git status: !`git status`
- Current branch: !`git branch --show-current`
- Remote branches: !`git branch -r | head -20`
- Existing feature branches: !`git branch -a | grep -E 'feat-|fix-|hotfix-' | tail -10`

## Parameters

`/branch-create [request]`

`request` can be:
- **Empty** → interactive mode: ask for type (feat/fix/hotfix), description, optional base branch
- **Natural language** → e.g. `/branch-create 新增登录页`、`/branch-create fix 修复滚动 bug 基于 master`
- **Explicit args** (power users): `<type> <description> [base_branch] [--ide=code|windsurf]`

Defaults: `base_branch=dev`, `ide=windsurf`

## Your task

### Step 0: Determine inputs

- **No argument** → prompt:
  ```
  Branch type? [1] feat  [2] fix  [3] hotfix
  Description?
  Base branch? (default: dev)
  ```
  Wait for reply, then proceed.
- **Natural language** → infer type (feat/fix/hotfix) + description + base branch from the phrase.
- **Explicit args** → parse positional + flags directly.

### Step 1: Build branch name

1. Parse user input for branch type, description, and base branch
2. Generate branch name with auto-versioning: `{type}_{description}_v{N}`
   - Check existing branches of same type for max version number
   - Increment version by 1
   - Translate Chinese description to English kebab-case
3. Create remote branch from base branch
4. Checkout local branch tracking remote
5. Optionally open in IDE
6. Report the created branch name

You MUST do all of the above in a single message. Do not send any other text or messages besides the tool calls.
