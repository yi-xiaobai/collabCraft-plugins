---
allowed-tools: Bash(git fetch:*), Bash(git branch:*), Bash(git checkout:*), Bash(git switch:*), Bash(git stash:*), Bash(git stash pop:*)
description: Smart switch between Git branches with fuzzy search
---

## Context

- Current branch: !`git branch --show-current`
- Recent branches (by last commit): !`git for-each-ref --sort=-committerdate refs/heads/ --format='%(refname:short) %(committerdate:relative)' | head -15`
- All local branches: !`git branch`
- Remote branches: !`git branch -r | head -20`
- Uncommitted changes: !`git status --short`

## Your task

Help user switch to a Git branch intelligently.

### Step 1: Parse user input

User may provide:
- Branch name (full or partial)
- Branch number from the list
- Fuzzy keyword (e.g., "login" → feat-user-login-v3)

### Step 2: Handle uncommitted changes

If there are uncommitted changes:
1. Ask user: "有未提交的变更，是否暂存(stash)后切换？"
2. If yes: `git stash push -m "auto-stash-before-switch"`
3. If no: Stop and inform user

### Step 3: Match branch

**Matching priority:**
1. Exact match with local branch
2. Fuzzy match with local branch (contains keyword)
3. Match with remote branch (create local tracking)

### Step 4: Switch branch

```bash
# Local branch
git checkout <branch_name>

# Or remote branch (create local tracking)
git checkout -b <branch_name> origin/<branch_name>
```

### Step 5: Restore stashed changes (if any)

```bash
git stash pop
```

### Output format

```
✅ 已切换到分支: <branch_name>
📊 分支状态: <ahead/behind info>
```

## Examples

```bash
/branch-switch              # Show recent branches to select
/branch-switch login        # Fuzzy match branches containing "login"
/branch-switch 3            # Switch to branch #3 from list
/branch-switch feat-auth    # Switch to feat-auth-v2
```
