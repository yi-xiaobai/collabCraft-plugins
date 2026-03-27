---
allowed-tools: Bash(npm:*), Bash(yarn:*), Bash(pnpm:*), Bash(cat:*), Bash(git:*), Bash(ls:*)
description: Full release workflow - build, version, publish, and push
---

## Context

- Current directory: !`pwd`
- Package info: !`cat package.json 2>/dev/null | grep -E '"name"|"version"' | head -3`
- Git branch: !`git branch --show-current`
- Git status: !`git status --porcelain 2>/dev/null | head -5`

## Parameters

User may specify: `/release [version-type] [--dry-run]`
- `version-type`: `patch` (default), `minor`, `major`
- `--dry-run`: Show what would happen without executing

## Your task

Execute the full release workflow: build → version → publish → git push.

### Step 1: Pre-flight Checks

1. Working directory must be clean
2. Must be on `main` or `master` branch (or user confirms)
3. Package must not be private

If `--dry-run`, show planned actions and stop.

### Step 2: Build

Detect package manager and run build:
```bash
<pm> run build
```

If build fails, stop immediately.

### Step 3: Version Bump

```bash
npm version <version-type> -m "chore(release): %s"
```

This creates commit and tag automatically.

### Step 4: Publish

```bash
npm publish
```

### Step 5: Push

```bash
git push && git push --tags
```

### Step 6: Report

Output summary:
```
✅ Released <package-name>@<version>
   - Build: success
   - Published to: <registry>
   - Git tag: v<version>
```

## Error Handling

- **Any step fails**: Stop immediately, report which step failed
- **Dirty working directory**: List uncommitted files
- **Wrong branch**: Warn and ask for confirmation
- **Build failure**: Show build errors
- **Publish failure**: Show npm error, suggest fixes

Execute all steps in sequence. Stop on first error.
