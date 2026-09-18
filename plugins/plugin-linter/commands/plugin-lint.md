---
allowed-tools: Bash(python3:*), Read
description: Validate plugin files and repository-level consistency
---

## Context

- Repository: !`git rev-parse --show-toplevel 2>/dev/null || pwd`

## Parameters

`/plugin-lint [path]`

Defaults: scan all plugin files and repository metadata under the current directory

## Your task

1. Resolve the optional path relative to the current repository.
2. Run `${CLAUDE_PLUGIN_ROOT}/scripts/lint_plugins.py --root . [path]` with
   Python 3.
3. Return the script's findings and exit status without converting errors into
   warnings.
4. Do not modify files unless the user separately asks for fixes.

You MUST do all of the above in a single message.
