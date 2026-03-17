---
allowed-tools: Bash(glab mr list:*)
description: List GitLab Merge Requests for current project
disable-tools-approval: true
---

## Parameters

User may specify: `/mr-list [--all]`
- Default: show current user's MRs only (`--author=@me`)
- `--all`: show all open MRs

## Your task

1. If `--all`: run `glab mr list --state opened`
2. Otherwise: run `glab mr list --state opened --author=@me`
3. Format output as markdown table with: MR number, title, author (--all only), branch, updated date

You MUST do all of the above in a single message. Do not send any other text or messages besides the tool calls.

## Output format

Default:
```
📋 **project/name** - 我的 MR 列表 (3)

| MR | Title | Branch | Updated |
|----|-------|--------|---------|
| [#42](https://...) | feat: add login | feat/login → dev | 2026-03-17 |
```

With `--all`:
```
📋 **project/name** - 所有 MR 列表 (5)

| MR | Title | Author | Branch | Updated |
|----|-------|--------|--------|---------|
| [#42](https://...) | feat: add login | zhangsan | feat/login → dev | 2026-03-17 |
```

## Configuration

Requires:
- `glab` CLI installed
- Run `glab auth login` to authenticate
