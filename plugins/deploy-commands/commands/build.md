---
allowed-tools: Bash(npm:*), Bash(yarn:*), Bash(pnpm:*), Bash(cat:*), Bash(ls:*)
description: Build the current project
---

## Context

- Current directory: !`pwd`
- Package manager: !`cat package.json 2>/dev/null | grep -E '"packageManager"|"scripts"' | head -5`
- Build scripts available: !`cat package.json 2>/dev/null | grep -E '"build|"compile|"dist' | head -5`

## Your task

Build the current project using the appropriate package manager and build command.

### Step 1: Detect Package Manager

Check for lock files in order:
- `pnpm-lock.yaml` → use `pnpm`
- `yarn.lock` → use `yarn`
- `package-lock.json` → use `npm`

### Step 2: Run Build

Execute the build command:
```bash
<package-manager> run build
```

If `build` script doesn't exist, check for alternatives:
- `compile`
- `dist`
- `bundle`

### Step 3: Report Result

- **Success**: Report build completed, show output directory if detected
- **Failure**: Show error output, suggest fixes

## Error Handling

- **Missing dependencies**: Suggest running `<pm> install` first
- **Build script not found**: List available scripts from package.json
- **Build errors**: Show relevant error lines, don't truncate

Execute build and report result concisely.
