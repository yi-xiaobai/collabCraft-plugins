# Weekly Report

Creates a concise weekly work summary from commits in the current Git
repository. The default period is the previous completed calendar week
(Monday through Sunday), matching the common weekly-report convention.

## Usage

```text
/weekly-report
/weekly-report 2026-09-09
/weekly-report --week 2026-W37
/weekly-report --since 2026-09-07 --until 2026-09-13
/weekly-report --author alice@example.com
/weekly-report --all-authors --refs current
```

The default author is the repository's configured `user.email`, falling back to
`user.name`. Commits are collected across all local refs so work remains visible
after switching branches. Use `--refs current` to inspect only `HEAD`.

The collector is read-only. It excludes merge commits, gathers commit messages
and changed paths as evidence, and leaves the final grouping and wording to the
model.
