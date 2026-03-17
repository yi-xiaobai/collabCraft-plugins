---
allowed-tools: Bash(git status:*), Bash(git log:*), Bash(git reset:*), Bash(git restore:*)
description: Undo the last commit while keeping changes
---

## Context

- Current branch: !`git branch --show-current`
- Last 5 commits: !`git log --oneline -5`
- Current status: !`git status --short`

## Your task

Undo the last commit while preserving changes.

### Step 1: Show what will be undone

```
📋 将撤销的提交:
<commit_hash> <commit_message>
Author: <author>
Date: <date>

📁 变更将保留在工作区:
<files changed>
```

### Step 2: Ask user for undo mode

Present options:
1. **Soft (推荐)**: Undo commit, keep changes staged
   ```bash
   git reset --soft HEAD~1
   ```
   Changes remain in staging area, ready to re-commit.

2. **Mixed**: Undo commit, unstage changes
   ```bash
   git reset --mixed HEAD~1
   ```
   Changes remain in working directory, but unstaged.

3. **Hard**: ⚠️ Undo commit AND discard changes
   ```bash
   git reset --hard HEAD~1
   ```
   **DANGER**: All changes will be lost!

### Step 3: Execute with confirmation

- For soft/mixed: Execute directly
- For hard: Require explicit confirmation "确认丢弃所有变更？输入 YES 继续"

### Step 4: Handle pushed commits

If the commit was already pushed:
```
⚠️  此提交已推送到远端！
撤销后需要 force push: git push --force

建议：如果其他人可能已拉取此提交，考虑使用 git revert 代替
```

### Step 5: Report result

```
✅ 已撤销提交: <commit_hash>
📝 变更状态: <staged/unstaged/discarded>
💡 下一步: 修改后重新提交，或使用 /commit
```

## Examples

```bash
/commit-undo           # Undo last commit (soft mode)
/commit-undo soft      # Keep changes staged
/commit-undo mixed     # Unstage changes
/commit-undo hard      # Discard all changes (with confirmation)
```

## Safety rules

- NEVER execute --hard without explicit confirmation
- ALWAYS warn if commit was pushed
- ALWAYS show what will be undone first
