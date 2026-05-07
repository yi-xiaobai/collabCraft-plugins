---
allowed-tools: Bash(git fetch:*), Bash(git log:*), Bash(git branch:*), Bash(glab mr update:*), Bash(glab mr view:*), Bash(glab api:*)
description: Generate MR title and description based on git commits, then update remote MR
---

## Context

- Current branch: !`git branch --show-current`
- MR info: !`glab mr view --output json 2>/dev/null | head -80`

## Your task

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

### Step 2: Generate content

**Delegate to the `mr-summarizer` subagent.** Pass it:
- The authoritative commit list from Step 1
- The `target_branch`

The subagent returns:
- A Conventional Commits title
- A bullet-list description with `≤ N` bullets (N = effective commits after revert-pair exclusion)

Do NOT inline title/description rules here — trust the subagent's output.

### Step 3: Update MR and report

Call `glab mr update` directly with the generated title and description, then print a summary:

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

You MUST do all of the above in a single message.
