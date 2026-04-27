---
allowed-tools: Bash(git status:*), Bash(git diff:*), Bash(git add:*), Bash(git commit:*), Bash(git push:*), Bash(glab mr create:*)
description: Commit, push, and create GitLab Merge Request
---

## Context

- Current git status: !`git status`
- Current git diff (staged and unstaged changes): !`git diff HEAD`
- Current branch: !`git branch --show-current`
- Recent commits: !`git log --oneline -5`

## Parameters

`/commit-push-mr [request]`

`request` can be:
- **Empty** → interactive mode: ask target branch and MR type
- **Natural language** → e.g. `/commit-push-mr 合到 main 草稿`、`/commit-push-mr draft to master`
- **Explicit args** (power users): `[target_branch] [--wip]`

Defaults: `target_branch=dev`, normal MR (not draft)

## Your task

### Step 0: Determine inputs

- **No argument** → prompt:
  ```
  Current branch: <current>

  Target branch? (default: dev)
  MR type? [1] normal  [2] --wip (draft)  (default: 1)
  ```
  Wait for reply.
- **Natural language** → infer `target_branch` (e.g. "main"/"master"/"dev") and whether WIP/draft is requested.
- **Explicit args** → use directly.

Based on the above changes:

1. Analyze the changes and generate a commit message using Conventional Commits format
2. Stage relevant files (avoid .env, credentials, secrets)
3. Create the commit
4. Push the branch to origin
5. Create a GitLab Merge Request:
   - `glab mr create --target-branch <branch> --fill --assignee @me --remove-source-branch --squash-before-merge [--draft] --yes`
6. Report the MR URL

You MUST do all of the above in a single message. Do not send any other text or messages besides the tool calls.

## Error Handling

- NEVER use `--no-verify` or `--force`
- If pre-commit check fails:
  - Style issues (lint, formatting): pre-commit auto-fixes them, re-stage modified files and commit again
  - Logic issues (branch naming, code errors): stop immediately and report the reason
- Other failures (push, mr create, etc.): stop immediately and report the reason
