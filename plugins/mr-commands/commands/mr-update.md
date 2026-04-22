---
allowed-tools: Bash(git branch:*), Bash(git branch -r:*), Bash(glab mr view:*), Bash(glab mr update:*)
description: Update MR metadata (target branch, assignee, reviewer, labels, draft status)
---

## Context

- Current branch: !`git branch --show-current`
- MR info: !`glab mr view --output json 2>/dev/null | head -60`
- Remote branches: !`git branch -r | head -20`

## Parameters

`/mr-update [flags]`

At least one flag is required:

| Flag | Example | Description |
|------|---------|-------------|
| `--target <branch>` | `--target main` | Change target branch |
| `--assignee <user>` | `--assignee @me` | Set assignee (`@me` for self) |
| `--reviewer <user>` | `--reviewer alice,bob` | Set reviewers (comma-separated) |
| `--label <labels>` | `--label bug,urgent` | Add labels |
| `--unlabel <labels>` | `--unlabel wip` | Remove labels |
| `--draft` | `--draft` | Mark as draft |
| `--ready` | `--ready` | Mark as ready (unset draft) |
| `--milestone <name>` | `--milestone v2.0` | Set milestone |

Multiple flags can be combined in one call.

## Your task

1. **Validate**: ensure MR exists on current branch (from MR info above)
   - If no MR found → report and abort with hint to run `/commit-push-mr`
   - If no flag provided → print usage table and abort

2. **Validate target branch** (if `--target` given):
   - Confirm the target branch exists in remote branches listed above
   - If not found → list available remote branches and abort (do NOT silently create)

3. **Map flags to `glab mr update` options**:
   - `--target X` → `--target-branch X`
   - `--assignee X` → `--assignee X`
   - `--reviewer X` → `--reviewer X`
   - `--label X` → `--label X`
   - `--unlabel X` → `--unlabel X`
   - `--draft` → `--draft`
   - `--ready` → `--ready`
   - `--milestone X` → `--milestone X`

4. **Execute**: run a single `glab mr update` combining all mapped options.
   - Do NOT touch title or description (that's `/mr-beautify`'s job)

5. **Report**: print before/after diff of changed fields.

## Output format

```
✏️ Updating MR !<iid> on branch <current-branch>

Changes:
  target_branch: <old> → <new>
  assignee:      <old> → <new>
  labels:        <old> → <new>

✅ MR updated: <web_url>
```

## Error Handling

- **No MR**: suggest running `/commit-push-mr` to create one first
- **No flags**: print usage table
- **Invalid target branch**: list available remote branches
- **glab failure**: surface error verbatim, do not retry

You MUST do all of the above in a single message.
