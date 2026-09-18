---
name: plugin-linter
description: Validate Claude and Codex plugin structure, manifests, marketplaces, and Markdown conventions. Use when checking a plugin repository or diagnosing plugin packaging problems.
---

# Plugin Linter

Run the bundled [validator](../../scripts/lint_plugins.py) against the requested
repository before forming conclusions:

```bash
python3 /resolved/plugin/path/scripts/lint_plugins.py --root /target/repository
```

- Pass an optional file or directory after `--root` when the user requests a
  narrow check.
- Treat errors as failures and warnings as review items.
- Do not modify files unless the user explicitly asks for fixes.
- Report the scanned file count, errors, warnings, and command exit status.
