---
allowed-tools: Bash(git fetch:*), Bash(git branch:*), Bash(git push:*), Bash(git checkout:*), Bash(open:*), Bash(code:*), Bash(windsurf:*)
description: Create a new Git branch — delegates slug generation to the `branch-namer` agent (≤3 words) and combines with feat/fix/hotfix (e.g. feat_add-login-page_v1)
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
- **Explicit args**: `<type> <description> [base_branch] [--ide=code|windsurf]`

Defaults: `base_branch=dev`, `ide=windsurf`

## Your task

Create a branch from the **remote** base branch, then **automatically check out (switch to) the new branch**, then optionally open in the IDE. Report the final branch name.

Rules:
- Resolve `type` (feat/fix/hotfix), `description`, and `base_branch` from the input. If input is empty, prompt the user with this block first and wait for the reply:
  ```
  Branch type? [1] feat  [2] fix  [3] hotfix
  Description?
  Base branch? (default: dev)
  ```
- `git fetch` the base branch first and branch off the up-to-date `origin/{base_branch}`, so the new branch is in sync with remote.
- Delegate slug generation to the `branch-namer` subagent (≤3-word kebab-case). Don't inline slug logic.
- Branch name format: `{type}_{slug}_v{N}` — auto-increment `N` past the max existing version of the same type.
- **Never include the base branch in the branch name.**

Do all of the above in a single message — tool calls only, no extra text.
