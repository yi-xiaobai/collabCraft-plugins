---
allowed-tools: Bash(git remote:*), Bash(curl *gitlab*:*), Bash(jq:*)
description: List GitLab Merge Requests for current project
disable-tools-approval: true
---

## Context

- Remote URL: !`git remote get-url origin`

## Parameters

User may specify: `/mr-list [--all]`
- Default: show current user's MRs only
- `--all`: show all open MRs

## Your task

1. Parse the remote URL to extract GitLab project path (e.g., `group/project`)
2. URL-encode the path (`/` → `%2F`)
3. Get current user ID via GitLab API (skip if `--all`)
4. Fetch MR list from GitLab API with appropriate filters
5. Format output as markdown table with: MR link, title, author (--all only), branch, updated date

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

Requires environment variables:
- `GITLAB_TOKEN`: GitLab Personal Access Token
- `GITLAB_HOST`: GitLab domain (e.g., gitlab.company.com)
