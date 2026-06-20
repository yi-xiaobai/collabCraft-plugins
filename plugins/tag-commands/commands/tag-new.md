---
allowed-tools: Bash(git tag:*), Bash(git log:*), Bash(git rev-parse:*), Bash(git config:*), Bash(git push:*)
description: Create a new debug-pri tag for the current user by bumping version
---

## Context
!`git rev-parse --abbrev-ref HEAD`

## Parameters
- No arguments: bump patch (default)
- `patch` / `minor` / `major`: semver bump level
- `<version>`: explicit version (e.g. `v2.0.0`)
- `--dry-run`: preview without creating

## Your task
1. Get current author name from git config
2. Compute name abbreviation (first letter of each name segment, lowercase)
3. Fetch all tags on current branch: `git tag --sort=-version:refname`
4. Determine bump type:
   - Explicit version → use directly, skip agent
   - `patch` / `minor` / `major` → use as bump type
   - Otherwise → default to `patch`
5. Delegate to `tag-pattern-analyzer` with abbreviation, bump type, and all branch tags
6. Display analysis: abbreviation, latest tag, suggested tag, reasoning
7. If `--dry-run`, stop here
8. Ask user to confirm the suggested tag (allow custom version input)
9. Create annotated tag: `git tag -a <final_tag> -m "debug-pri: <abbr> <version>"`
10. Push: `git push origin <final_tag>`
11. You MUST do all of the above in a single message.
