---
name: dependency-upgrade
description: Upgrade @master/turtle and deliver the verified change through a versioned branch and GitLab merge request. Use when the user asks to upgrade turtle or prepare its upgrade MR.
---

# Dependency Upgrade

Upgrade only `@master/turtle`. Do not generalize this workflow to unrelated
dependencies without an explicit request.

## Resolve inputs

- Accept a target version or `latest`; default to `latest` when the user asks
  for an upgrade without naming a version.
- Accept `dev` or `master` as the base branch; default to `dev`.
- When the request contains neither a version nor a clear intent to use the
  latest version, ask one question before modifying files.

## Workflow

1. Read the current version from `package.json` and confirm the selected base
   branch exists.
2. Update the base branch, then create `chore_upgrade-turtle_vN`, where `N` is
   one greater than the highest matching local or remote branch version.
3. Update the package version and run `pnpm install` so the lockfile stays in
   sync.
4. Run the repository's relevant checks and review the complete diff.
5. Commit, push with upstream tracking, and create a GitLab merge request to the
   selected base branch. Assign it to the current user, remove the source branch
   after merge, and squash before merge.

## Safety and recovery

- Never use `--no-verify` or force-push.
- Fix only clear, in-scope source formatting, lint, type, or test failures caused
  by the upgrade, then retry the failed step.
- Stop on registry, authentication, infrastructure, security threshold, or
  ambiguous failures. Do not weaken checks or configuration.
- Report the old and new versions, verification result, commit, and merge
  request URL.
