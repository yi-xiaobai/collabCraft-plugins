---
allowed-tools: Bash(git log:*), Bash(git branch:*), Bash(git merge-base:*), Bash(glab mr update:*), Bash(glab mr list:*)
description: Generate MR title and description based on git commits, then update remote MR
---

## Parameters

User may specify: `/mr-title [target-branch]`
- Default: `dev`

## Context

- Current branch: !`git branch --show-current`
- Commits to merge: !`git log origin/dev..HEAD --oneline --no-merges 2>/dev/null || git log dev..HEAD --oneline --no-merges`

## Your task

Based on the above commits, generate MR title and description, then update remote MR.

1. Analyze commits to determine primary change type (feat > fix > refactor > chore)
2. Generate title: `{type}: {中文概述}`
3. Generate description: 每个 commit 提炼为一条简洁的中文变更点
   - **忽略**: revert 类型的 commit 及其对应的原 commit
4. Find MR for current branch: `glab mr list --source-branch={current-branch}`
5. Update MR: `glab mr update {mr-id} --title "{title}" --description "{description}"`

## Output format

```
📝 **MR Title**

{type}: {中文概述}

📄 **MR Description**

- {变更点1}
- {变更点2}
- {变更点3}

✅ MR #{mr-id} 已更新
```

## Error Handling

- **No commits**: 当前分支相对目标分支没有新提交
- **Branch not found**: 建议检查分支名或 `git fetch`
- **No MR found**: 当前分支没有关联的 MR，建议先创建 MR

You MUST do all of the above in a single message.
