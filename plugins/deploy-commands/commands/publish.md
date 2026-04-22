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

`/publish [request]`

`request` can be:
- **Empty** → interactive mode: show current version and ask which bump + tag
- **Natural language** → e.g. `/publish 升个中版本`、`/publish major beta`
- **Explicit args** (power users): `[patch|minor|major] [--tag=<tag>]`

Defaults: `version-type=patch`, no dist-tag

## Your task

### Step 0: Determine inputs

- **No argument** → prompt:
  ```
  Current version: <version>

  Version bump?
    [1] patch  (x.y.Z)
    [2] minor  (x.Y.0)
    [3] major  (X.0.0)

  npm dist-tag? (blank = latest, e.g. beta / next)
  ```
  Wait for reply.
- **Natural language** → infer bump type + tag.
- **Explicit args** → use directly.

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

You MUST do all of the above in a single message.
