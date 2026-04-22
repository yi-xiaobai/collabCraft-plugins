---
allowed-tools: Bash(git:*), Bash(pnpm:*), Bash(glab:*), Edit
description: Upgrade @master/turtle package version
---

## Context

- Current branch: !`git branch --show-current`
- Current turtle version: !`grep '"@master/turtle"' package.json | head -1`

## Parameters

`/turtle-upgrade [request]`

`request` can be:
- **Empty** → interactive mode: show current turtle version and ask for target version + base branch
- **Natural language** → e.g. `/turtle-upgrade 升到最新`、`/turtle-upgrade 2.3.1 基于 master`
- **Explicit args** (power users): `[version] [--branch dev|master]`

Defaults: `version=latest`, `branch=dev`

## Task

### Step 0: Determine inputs

- **No argument** → prompt:
  ```
  Current @master/turtle: <current-version>

  Target version? (blank = latest)
  Base branch? [1] dev  [2] master  (default: 1)
  ```
  Wait for reply.
- **Natural language** → infer version + base branch.
- **Explicit args** → use directly.

### Step 1: Execute

1. Create branch `chore_upgrade_turtle_<version>` from `<branch>`
2. Update `@master/turtle` version in package.json, run `pnpm i`
3. Commit, push, create MR to `<branch>` with:
   - Assignee: current user (`--assignee @me`)
   - Delete source branch after merge (`--remove-source-branch`)
   - Squash commits (`--squash-before-merge`)
4. Report MR URL

You MUST do all of the above in a single message.
