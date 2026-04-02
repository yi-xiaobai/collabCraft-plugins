---
allowed-tools: Bash(git log:*), Bash(git branch:*), Bash(git merge-base:*)
description: Generate MR title and description based on git commits
---

## Parameters

User may specify: `/mr-title [target-branch]`
- Default: `dev`

## Context

- Current branch: !`git branch --show-current`
- Commits to merge: !`git log origin/dev..HEAD --oneline --no-merges 2>/dev/null || git log dev..HEAD --oneline --no-merges`

## Your task

Based on the above commits, generate MR title and description.

1. Analyze commits to determine primary change type (feat > fix > refactor > chore)
2. Generate title: `{type}({scope}): {summary}` (max 72 chars)
3. Generate description using template below

## Output format

```
📝 **MR Title**

{type}({scope}): {summary}

📄 **MR Description**

## 变更概述

{One paragraph summary}

## 主要变更

- **{type}**: {description}

## 提交记录

| Commit | Message |
|--------|---------|
| {hash} | {message} |
```

## Error Handling

- **No commits**: 当前分支相对目标分支没有新提交
- **Branch not found**: 建议检查分支名或 `git fetch`

You MUST do all of the above in a single message.
