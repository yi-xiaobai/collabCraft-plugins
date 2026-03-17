---
allowed-tools: Bash(git fetch:*), Bash(git branch:*), Bash(git branch -d:*), Bash(git branch -D:*), Bash(git push origin --delete:*)
description: Clean up merged or stale Git branches
---

## Context

- Current branch: !`git branch --show-current`
- Default branch (main/master/dev): !`git remote show origin | grep 'HEAD branch' | cut -d: -f2`
- Local branches with last commit date: !`git for-each-ref --sort=-committerdate refs/heads/ --format='%(refname:short) | %(committerdate:relative)'`
- Merged branches: !`git branch --merged origin/main 2>/dev/null || git branch --merged origin/master 2>/dev/null || git branch --merged origin/dev`
- Remote branches: !`git branch -r`

## Your task

Help user clean up Git branches safely.

### Step 1: Analyze branches

Categorize branches:
1. **Safe to delete (merged)**: Branches merged into main/master/dev
2. **Stale (>30 days)**: Branches with no recent activity
3. **Protected**: main, master, dev, develop - never delete

### Step 2: Show cleanup options

Present options to user:
```
📦 可清理的分支:

已合并到 main/master:
  - feat-user-login-v1 (merged 2 days ago)
  - fix-bug-123-v2 (merged 5 days ago)

长期未更新 (>30天):
  - feat-old-feature-v1 (last commit 45 days ago)

当前分支: feat-new-feature-v3 [跳过]
保护分支: main, master, dev [跳过]
```

### Step 3: Confirm and delete

Ask user which branches to delete:
- "输入要删除的分支编号（多个用空格分隔），或输入 'merged' 删除所有已合并分支"

**Delete local branch:**
```bash
git branch -d <branch_name>    # Safe delete (checks merge status)
git branch -D <branch_name>    # Force delete (use with caution)
```

**Delete remote branch (with confirmation):**
```bash
git push origin --delete <branch_name>
```

### Step 4: Report results

```
✅ 已删除本地分支: feat-user-login-v1, fix-bug-123-v2
⚠️  无法删除: feat-active-work (未合并)
```

## Safety rules

- NEVER delete: main, master, dev, develop
- NEVER delete current branch
- ALWAYS confirm before deleting remote branches
- ALWAYS confirm before force delete (-D)
- Check merge status before safe delete (-d)

## Examples

```bash
/branch-delete              # Show cleanup options
/branch-delete merged       # Delete all merged branches
/branch-delete feat-old-v1  # Delete specific branch
```
