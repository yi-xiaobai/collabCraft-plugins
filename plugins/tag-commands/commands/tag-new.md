---
allowed-tools: Bash(git tag:*), Bash(git log:*), Bash(git rev-parse:*), Bash(git config:*), Bash(git push:*)
description: Create a new debug-pri tag for the current user by bumping version
---

## Context
!`git rev-parse --abbrev-ref HEAD`

## Parameters
- No arguments: bump patch (default)
- `patch` / `minor` / `major`: semver bump level
- `<version>`: explicit version (e.g. `v2.0.0`)
- `--dry-run`: preview without creating

## Your task
1. Run `git config user.name` to get the current author name
2. Run the following to compute name abbreviation:
   `python3 -c "import sys,unicodedata; n=sys.argv[1]; r=''; cn=False; for c in n: cat=unicodedata.category(c); is_cn=cat.startswith('Lo') and ('CJK' in unicodedata.name(c,'') or 'IDEOGRAPH' in unicodedata.name(c,'')); is_alnum=cat.startswith('L') or cat.startswith('N'); if is_cn: if not cn: r+=c; cn=True; elif is_alnum: r+=c; cn=False; else: cn=False; print(r[:8].lower())" "$(git config user.name)"`
3. Fetch all tags for this user: `git tag -l "debug-pri-<abbr>-v*" --sort=-version:refname`
4. Determine bump type:
   - If user provided explicit version → use it directly, skip agent
   - If user provided patch/minor/major → use as bump_type
   - Otherwise → default to `patch`
5. Delegate to `tag-pattern-analyzer` subagent with: user abbreviation, bump_type (or explicit version), and full tag list
6. Display the analysis:
   - Your abbreviation: `<abbr>`
   - Latest tag: `<latest_tag>`
   - Suggested new tag: `<suggested_tag>`
   - Reasoning: `<reasoning>`
7. If `--dry-run`, stop here
8. Ask user to confirm the suggested tag (allow custom version input)
9. Create annotated tag: `git tag -a <final_tag> -m "debug-pri: <abbr> <version>"`
10. Push: `git push origin <final_tag>`
11. You MUST do all of the above in a single message.
