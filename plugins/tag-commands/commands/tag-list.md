---
allowed-tools: Bash(git tag:*), Bash(git log:*), Bash(git rev-parse:*), Bash(git config:*)
description: List tags grouped by service name
---

## Context
!`git rev-parse --abbrev-ref HEAD`
!`git tag -l "*" --sort=-version:refname`

## Parameters
- No arguments: list all tags grouped by service name
- `<name>`: filter by service name (e.g. `backend`, `frontend`)

## Your task
1. Get current author name from git config
2. Compute name abbreviation (first letter of each name segment, lowercase)
3. Fetch tags: all tags, or filtered by name prefix if provided
4. For each tag, retrieve tag name, commit SHA (short), and commit date
5. Group tags by service name (the prefix before the version, e.g. `name` from `name-v1.0.0`)
6. Present in a clean grouped table format
7. You MUST do all of the above in a single message.
