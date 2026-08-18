---
allowed-tools: Bash(glab mr list:*)
description: List GitLab Merge Requests for current project
disable-tools-approval: true
---

## Context

- Current project: !`git remote get-url origin 2>/dev/null | sed 's/.*[:/]\([^/]*\/[^/]*\)\.git/\1/'`

## Parameters

`/mr-list [--all]`

Defaults: show current user's MRs only

## Your task

1. If `--all`: run `glab mr list`
2. Otherwise: run `glab mr list --author=@me`
3. Format output as markdown table with: MR number, title, author (--all only), branch, updated date

You MUST do all of the above in a single message.

## Output format

Default:
```
📋 **project/name** - My MR List (3)

| MR | Title | Branch | Updated |
|----|-------|--------|---------|
| [#42](https://...) | feat: add login | feat/login → dev | 2026-03-17 |
```

With `--all`:
```
📋 **project/name** - All MR List (5)

| MR | Title | Author | Branch | Updated |
|----|-------|--------|--------|---------|
| [#42](https://...) | feat: add login | zhangsan | feat/login → dev | 2026-03-17 |
```

## Configuration

Requires:
- `glab` CLI installed
- Run `glab auth login` to authenticate
