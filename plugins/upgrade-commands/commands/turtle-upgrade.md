---
allowed-tools: Bash(git:*), Bash(pnpm:*), Bash(glab:*), Edit
description: Upgrade @master/turtle package version
---

## Context

- Current branch: !`git branch --show-current`
- Current turtle version: !`grep '"@master/turtle"' package.json | head -1`

## Parameters

`/turtle-upgrade [version] [--from dev|master] [--to dev|master]`

Defaults: version=latest, from=dev, to=dev

## Task

1. Create branch `chore_upgrade_turtle_<version>` from `<from>`
2. Update `@master/turtle` version in package.json, run `pnpm i`
3. Commit, push, create MR (with squash enabled)
4. Report MR URL
