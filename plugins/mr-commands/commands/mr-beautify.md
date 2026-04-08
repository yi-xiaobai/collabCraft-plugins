---
allowed-tools: Bash(git log:*), Bash(git branch:*), Bash(glab mr update:*), Bash(glab mr view:*)
description: Generate MR title and description based on git commits, then update remote MR
---

## Parameters

`/mr-beautify [target-branch]`

Defaults: target-branch=dev

## Context

- Current branch: !`git branch --show-current`
- Commits to merge: !`git log origin/$1..HEAD --oneline --no-merges 2>/dev/null || git log $1..HEAD --oneline --no-merges`

## Your task

Based on the commits from current branch (shown above), generate MR title and description, then update remote MR.

1. Analyze commits to determine primary change type (feat > fix > refactor > chore)
2. Generate title based ONLY on the commit messages: `{type}: {summary}`
3. Generate description: extract each commit into a concise change point
   - **Ignore**: revert commits and their original commits (exclude pairs)
4. Find MR for current branch and update it:
   - Use `glab mr view` to check if MR exists for current branch
   - Use `glab mr update` to update title and description

## Error Handling

- **No commits**: no new commits relative to target branch
- **No MR found**: suggest creating MR first

You MUST do all of the above in a single message.
