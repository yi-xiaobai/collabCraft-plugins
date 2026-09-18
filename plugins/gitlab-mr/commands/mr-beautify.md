---
allowed-tools: Bash(git fetch:*), Bash(git log:*), Bash(git branch:*), Bash(glab mr update:*), Bash(glab mr view:*), Bash(glab api:*)
description: Generate MR title and description based on git commits, then update remote MR
---

## Context

- Current branch: !`git branch --show-current`
- MR info: !`glab mr view --output json 2>/dev/null | head -80`

## Your task

Apply the `gitlab-mr` skill.

Generate MR title and description based ONLY on the **actual commits in this MR** (from GitLab API, not from stale local refs), then update remote MR after user confirmation.

### Step 1: Get authoritative commit list

**DO NOT trust local `origin/{target_branch}` without fetching** — stale refs cause phantom commits from other MRs to leak into the list.

1. From MR info above, extract `target_branch` and `iid` (MR number)
2. Fetch the MR's real commit list from GitLab (source of truth):
   ```
   glab api "projects/:fullpath/merge_requests/{iid}/commits"
   ```
3. Cross-check with a fresh local diff:
   ```
   git fetch origin {target_branch}
   git log --oneline --no-merges --first-parent origin/{target_branch}..HEAD
   ```
4. If the two lists differ, **trust the glab API result** and warn the user.

### Step 2: Generate and preview content

Generate the title and description directly from the authoritative commit list:

- Title format: `{type}(scope): {imperative summary}`, no more than 72
  characters, with no trailing period.
- Choose the dominant type using this priority: `feat`, `fix`, `refactor`,
  `perf`, `test`, `docs`, `chore`.
- Use no more bullets than effective commits after excluding merge commits,
  revert pairs, and pure formatting commits.
- Group related commits and describe user-facing changes. Do not copy commit
  messages verbatim or invent changes.

Show the authoritative commits, proposed title, and proposed description. Ask
for confirmation before changing the remote MR, then stop.

### Step 3: Update MR after confirmation

Only after the user explicitly confirms the preview, call `glab mr update` with
the proposed title and description, then print:

```
📋 MR commits (from GitLab API): N commits
  1. <hash> <message>
  2. <hash> <message>
  ...

📝 Title:
  <title>

📝 Description:
  - <bullet 1>
  - <bullet 2>

✅ MR updated
```

## Error Handling

- **No commits**: no new commits relative to target branch → abort
- **No MR found**: suggest creating MR first
- **glab api fails**: fall back to `git log` but warn user that result may be inaccurate
- **Content changes before confirmation**: re-fetch the authoritative commit
  list and regenerate the preview
