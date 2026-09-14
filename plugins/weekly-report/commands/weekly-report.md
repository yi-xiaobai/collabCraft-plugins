---
allowed-tools: Bash(python3:*), Bash(git rev-parse:*), Bash(git config:*), Bash(date:*), Read
description: Summarize Git commits into a weekly work report
---

## Context

- Repository: !`git rev-parse --show-toplevel 2>/dev/null || echo "Not a Git repository"`
- Git identity: !`git config user.email 2>/dev/null || git config user.name 2>/dev/null || echo "Not configured"`
- Local date: !`date +%Y-%m-%d`

## Parameters

`/weekly-report [YYYY-MM-DD | --date YYYY-MM-DD | --week YYYY-Www | --since YYYY-MM-DD --until YYYY-MM-DD] [--author PATTERN | --all-authors] [--refs all|current]`

Defaults: period=previous completed Monday-through-Sunday week, author=current Git identity, refs=all

## Your task

1. Parse `$ARGUMENTS`. Treat a bare date as `--date`; natural-language dates
   may be normalized only when unambiguous.
2. Run `${CLAUDE_PLUGIN_ROOT}/scripts/collect_weekly_commits.py` with the
   resolved options. Do not calculate week boundaries independently.
3. Apply the `weekly-report` skill to the returned JSON and produce the final
   report. Do not include the raw JSON unless requested.
4. If collection fails, report the error and the accepted parameter forms.

You MUST do all of the above in a single message.
