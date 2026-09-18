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
- **Natural language** → e.g. `/turtle-upgrade to latest` or `/turtle-upgrade 2.3.1 from master`
- **Explicit args** (power users): `[version] [--branch dev|master]`

Defaults: `version=latest`, `branch=dev`

## Task

Apply the `dependency-upgrade` skill. The command behavior below is the Claude
Code entry point for that shared workflow.

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

1. Create branch `chore_upgrade-turtle_vN` from `<branch>`, where `N` is one
   greater than the highest matching local or remote branch version
2. Update `@master/turtle` version in package.json, run `pnpm i`
3. Commit, push, create MR to `<branch>` with:
   - Assignee: current user (`--assignee @me`)
   - Delete source branch after merge (`--remove-source-branch`)
   - Squash commits (`--squash-before-merge`)
4. Report MR URL

When arguments are present and unambiguous, execute all steps sequentially in
one response. Interactive mode must stop after showing the prompt and wait for
the user's reply.

## Error Handling

- NEVER use `--no-verify` or `--force`
- If a pre-commit check fails, fix only clear source lint, formatting, type, or
  test failures caused by the upgrade, then retry the commit.
- Stop and report infrastructure, threshold, environment, or ambiguous failures.
- Never weaken hooks, tests, baselines, or thresholds to make the commit pass.
- Other failures (push, mr create, etc.): stop immediately and report the reason
