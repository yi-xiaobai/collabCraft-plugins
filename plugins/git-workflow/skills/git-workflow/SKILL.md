---
name: git-workflow
description: Apply CollabCraft team conventions when creating branches, committing changes, pushing, resolving pre-commit failures, or delivering work through a GitLab merge request. Use for Git write operations in a team repository; do not use for read-only Git inspection.
---

# Team Git Workflow

Use the model's native Git capabilities for ordinary operations. This skill only
adds team-specific decisions, safety boundaries, and delivery defaults.

## Branches

- Start new work from the user-specified base branch; default to `dev` when none
  is given.
- Update the base branch before creating the work branch.
- Name work branches `{type}_{slug}_v{N}`.
- Use `feat`, `fix`, `hotfix`, `refactor`, or `chore` as the type.
- Write the slug in lowercase kebab-case with no more than three words.
- Set `N` to one greater than the highest matching branch version, starting at
  `v1`.
- Do not change branches while the worktree is dirty without asking whether to
  commit or stash the changes.

## Commits

- Review the complete staged and unstaged diff before staging files.
- Do not stage secrets, credentials, `.env` files, or unrelated changes.
- Keep unrelated changes in separate commits.
- Use Conventional Commits: `type(scope): imperative subject`.
- Prefer a specific lowercase kebab-case scope for localized changes.
- Keep the subject at or below 72 characters and omit the trailing period.
- Add a body only when the reason or migration impact is not clear from the
  subject.
- Never bypass repository checks with `--no-verify`.

## Pre-commit Failures

- Fix source lint, formatting, type, and test failures only when the correction
  is clear and remains within the requested change.
- Retry the original commit after a valid source fix.
- Stop and report infrastructure failures, security or quality threshold
  failures, environment problems, and ambiguous fixes.
- Never weaken hooks, tests, baselines, thresholds, or configuration merely to
  make a commit pass.

## Push And Merge Requests

- Never force-push unless the user explicitly requests it and the impact has
  been checked.
- Push the current branch with upstream tracking when needed.
- Default GitLab merge requests to `dev` unless the user specifies another
  target.
- Assign the merge request to the current user, remove the source branch after
  merge, and squash before merge.
- Create a draft only when requested.
- Preview remote or destructive actions when their intent is ambiguous.

## Verification

After a write operation, report the branch or commit created and confirm the
worktree and upstream status. Do not narrate routine Git commands.
