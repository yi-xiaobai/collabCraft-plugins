---
allowed-tools: Bash(git status:*), Bash(git diff:*), Bash(git add:*), Bash(git commit:*), Bash(git push:*), Bash(git branch:*), Bash(glab mr create:*)
description: Commit the current change, push it, and create a GitLab merge request with team defaults
---

## Context

- Current status: !`git status --short --branch`
- Current changes: !`git diff HEAD --`
- Current branch: !`git branch --show-current`
- Recent commits: !`git log --oneline -5 2>/dev/null || echo "No commits yet"`

## Parameters

`/commit-push-mr [request]`

The request may name a target branch or ask for a draft merge request. The
default target is `dev` and the default is a normal merge request.

## Your task

Apply the `git-workflow` skill and complete the delivery workflow:

1. Review all changes and stop if they contain secrets or unrelated work.
2. Stage the intended files and create one Conventional Commit. If there are
   unrelated changes, propose separate commits instead of combining them.
3. Push the current branch with upstream tracking when needed.
4. Create a GitLab merge request with the resolved target branch, assign it to
   the current user, remove the source branch after merge, and squash before
   merge. Create a draft only when requested.
5. Report the commit and merge request URL.

Never bypass checks or force-push. Handle pre-commit failures according to the
skill. Execute each step sequentially and stop when a step fails.
