---
allowed-tools: Bash(git fetch:*), Bash(git branch:*), Bash(git checkout:*), Bash(git pull:*), Bash(git merge:*), Bash(git status:*), Bash(git diff:*), Bash(git merge --abort:*), Bash(git add:*), Bash(git commit:*)
description: Merge a branch into current branch with conflict resolution
---

## Context

- Current branch: !`git branch --show-current`
- Current branch status: !`git status --short`
- Local branches: !`git branch`
- Remote branches: !`git branch -r | head -20`
- Uncommitted changes: !`git diff --stat HEAD`

## Parameters

`/branch-merge <source_branch> [--no-ff] [--squash]`

- `source_branch`: Branch to merge into current branch (required)
- `--no-ff`: Force a merge commit even if fast-forward is possible
- `--squash`: Squash all commits into one

## Your task

1. **Pre-check**:
   - Verify source branch exists (local or remote)
   - Check for uncommitted changes on current branch
   - If uncommitted changes exist, ask user to commit/stash first

2. **Update source branch**:
   - Run `git fetch origin`
   - If source branch has remote, pull latest: `git checkout <source> && git pull && git checkout <current>`
   - Report if source branch is up-to-date

3. **Execute merge**:
   - Run `git merge <source_branch>` (with flags if specified)
   - If fast-forward merge, report success

4. **Handle conflicts** (if any):
   - List conflicting files: `git diff --name-only --diff-filter=U`
   - For each conflict, show the diff and ask user:
     - **Accept ours**: Keep current branch version
     - **Accept theirs**: Keep source branch version
     - **Manual**: User will resolve manually
   - After resolution, stage files and complete merge commit

5. **Report result**:
   - Show merge status
   - Show commit log of merged changes

## Conflict resolution

When conflicts occur, present options:

```
⚠️ Merge conflict in: <filename>

Options:
1. Accept OURS (current branch: <current>)
2. Accept THEIRS (source branch: <source>)
3. Manual resolution (I'll fix it myself)

Which option? [1/2/3]
```

## Safety rules

- NEVER force merge without user confirmation on conflicts
- ALWAYS fetch latest before merging
- ALWAYS show conflict details before resolution
- If user chooses manual, run `git merge --abort` is NOT automatic - let user resolve

You MUST do all of the above in a single message. Do not send any other text or messages besides the tool calls.
