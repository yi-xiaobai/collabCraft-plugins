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

1. Stage relevant files (avoid `.env`, credentials, secrets)
2. **Delegate message generation to the `commit-message-writer` subagent**
   - The subagent reads the staged diff and returns a Conventional Commits message
   - Do NOT inline message rules here — trust the subagent's output
3. Create the commit with the returned message
4. Push to remote origin
5. Report the push result

You MUST do all of the above in a single message. Do not send any other text or messages besides the tool calls.

## Error Handling

- NEVER use `--no-verify` or `--force`
- If pre-commit check fails:
  - Style issues (lint, formatting): pre-commit auto-fixes them, re-stage modified files and commit again
  - Logic issues (branch naming, code errors): stop immediately and report the reason
- Other failures (push, etc.): stop immediately and report the reason
