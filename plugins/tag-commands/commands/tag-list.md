---
allowed-tools: Bash(git tag:*), Bash(git log:*), Bash(git rev-parse:*), Bash(git config:*)
description: List debug-pri tags grouped by service name
---

## Context
!`git rev-parse --abbrev-ref HEAD`
!`git tag -l "debug-pri-*" --sort=-version:refname`

## Parameters

`/tag-list [filter]`

`filter` can be:

- **Empty** → list all `debug-pri-*` tags grouped by service name, showing the latest 5 tags per service
- **Service name** → filter by a specific service, e.g. `/tag-list backend` to show only tags for the `backend` service

Defaults: show all services, 5 most recent tags per group.

## Your task
1. Run `git config user.name` to get the current author name
2. Compute the name abbreviation using this python one-liner:
   `python3 -c "import sys,unicodedata; n=sys.argv[1]; r=''; cn=False; for c in n: cat=unicodedata.category(c); is_cn=cat.startswith('Lo') and ('CJK' in unicodedata.name(c,'') or 'IDEOGRAPH' in unicodedata.name(c,'')); is_alnum=cat.startswith('L') or cat.startswith('N'); if is_cn: if not cn: r+=c; cn=True; elif is_alnum: r+=c; cn=False; else: cn=False; print(r[:8].lower())" "$(git config user.name)"`
3. If a `filter` argument was provided, use it as the service name directly; otherwise, fetch all tags matching `debug-pri-*`
4. For each tag, retrieve: tag name, commit SHA (short), and commit date
5. Group tags by service name (the part between `debug-pri-` and `-vX.Y.Z`)
6. Present in a clean grouped table format
7. You MUST do all of the above in a single message.
