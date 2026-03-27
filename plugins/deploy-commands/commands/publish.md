---
allowed-tools: Bash(npm:*), Bash(yarn:*), Bash(pnpm:*), Bash(cat:*), Bash(git:*)
description: Publish package to npm registry
---

## Context

- Current directory: !`pwd`
- Package info: !`cat package.json 2>/dev/null | grep -E '"name"|"version"|"private"' | head -5`
- Git status: !`git status --porcelain 2>/dev/null | head -5`
- Current registry: !`npm config get registry 2>/dev/null`

## Parameters

User may specify: `/publish [version-type] [--tag=<tag>]`
- `version-type`: `patch` (default), `minor`, `major`, `prepatch`, `preminor`, `premajor`, `prerelease`
- `--tag`: npm dist-tag (e.g., `beta`, `next`)

## Your task

Publish the current package to npm registry.

### Step 1: Pre-flight Checks

1. Ensure working directory is clean (no uncommitted changes)
2. Check package is not marked as `"private": true`
3. Verify user is logged in: `npm whoami`

### Step 2: Version Bump (if requested)

```bash
npm version <version-type> --no-git-tag-version
```

### Step 3: Publish

```bash
npm publish [--tag <tag>]
```

### Step 4: Post-publish

If version was bumped:
```bash
git add package.json package-lock.json
git commit -m "chore(release): v<new-version>"
git tag v<new-version>
git push && git push --tags
```

## Error Handling

- **Not logged in**: Prompt user to run `npm login`
- **Private package**: Inform user and stop
- **Version conflict**: Suggest incrementing version
- **Uncommitted changes**: List changes and ask user to commit first

Report publish result with package name and version.
