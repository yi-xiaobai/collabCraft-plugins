---
allowed-tools: Bash(git log:*), Bash(git branch:*), Bash(glab mr update:*), Bash(glab mr view:*)
description: Generate MR title and description based on git commits, then update remote MR
---

## Context

- Current branch: !`git branch --show-current`
- MR info: !`glab mr view --output json 2>/dev/null | head -50`

## Your task

Generate MR title and description based ONLY on the "Commits to merge" shown above, then update remote MR.

1. From MR info above, get the `target_branch`
2. Get commits: `git log --oneline --no-merges --first-parent origin/{target_branch}..HEAD`
3. Analyze commits to determine primary change type (feat > fix > refactor > chore)
4. Generate title based ONLY on the commit messages: `{type}: {summary}`
5. Generate description based ONLY on the commit messages: extract each commit into a concise change point
   - **Ignore**: revert commits and their original commits (exclude pairs)
6. Use `glab mr update` to update title and description

## Error Handling

- **No commits**: no new commits relative to target branch
- **No MR found**: suggest creating MR first

You MUST do all of the above in a single message.
