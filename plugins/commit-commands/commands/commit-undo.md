---
allowed-tools: Bash(git status:*), Bash(git log:*), Bash(git reset:*), Bash(git restore:*)
description: Undo the last commit while keeping changes
---

## Context

- Current branch: !`git branch --show-current`
- Last 5 commits: !`git log --oneline -5`
- Current status: !`git status --short`

## Parameters

`/commit-undo [request]`

`request` can be:
- **Empty** → interactive mode: show last commit and ask which mode
- **Natural language** → e.g. `/commit-undo 保留改动`、`/commit-undo discard everything`
- **Explicit args** (power users): `soft|mixed|hard`

Defaults: `soft` (keep changes staged)

Modes:
- `soft` — undo commit, keep changes staged
- `mixed` — undo commit, keep changes unstaged
- `hard` — undo commit and DISCARD all changes (destructive)

## Your task

### Step 0: Determine inputs

- **No argument** → show last commit + prompt:
  ```
  Last commit: <hash> <message>

  Undo mode?
    [1] soft   — keep changes staged (default, safest)
    [2] mixed  — keep changes unstaged
    [3] hard   — DISCARD all changes (destructive, requires "YES")
  ```
  Wait for reply.
- **Natural language** → map intent:
  - "保留/keep" → soft / mixed depending on "staged"
  - "丢弃/discard/reset" → hard (still require YES confirmation)
- **Explicit args** → use directly.

1. Show what will be undone (commit hash, message, author, files)
2. Execute the appropriate reset mode:
   - Soft: `git reset --soft HEAD~1`
   - Mixed: `git reset --mixed HEAD~1`
   - Hard: Require explicit "YES" confirmation first
3. Warn if commit was already pushed (requires force push)
4. Report result and next steps

## Safety rules

- NEVER execute --hard without explicit confirmation
- ALWAYS warn if commit was pushed
- ALWAYS show what will be undone first

You MUST do all of the above in a single message. Do not send any other text or messages besides the tool calls.
