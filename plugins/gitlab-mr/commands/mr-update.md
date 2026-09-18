---
allowed-tools: Bash(git branch:*), Bash(git branch -r:*), Bash(glab mr view:*), Bash(glab mr update:*)
description: Update MR metadata (target branch, assignee, reviewer, labels, draft status)
---

## Context

- Current branch: !`git branch --show-current`
- MR info: !`glab mr view --output json 2>/dev/null | head -60`
- Remote branches: !`git branch -r | head -20`

## Parameters

`/mr-update [request]`

`request` can be:
- **Empty** → enter interactive mode (show current state + menu)
- **Natural language** → e.g. `/mr-update target main` or `/mr-update assign to me`
- **Explicit flags** (power users) — see [Supported fields](#supported-fields)

## Your task

Apply the `gitlab-mr` skill.

### Step 1: Validate MR exists

From MR info above, confirm MR exists on current branch.
- No MR → abort and suggest installing `git-workflow` or creating the MR with
  `glab mr create`

### Step 2: Determine what to change

**If no argument given** → enter interactive mode:

```
📋 MR !<iid> current state:
  target_branch: <value>
  assignee:      <value>
  reviewer:      <value>
  labels:        <value>
  draft:         <true/false>
  milestone:     <value>

What would you like to change?
  1. Target branch
  2. Assignee
  3. Reviewer
  4. Labels (add / remove)
  5. Toggle draft status
  6. Milestone

Reply with a number, or describe in natural language
(e.g. "target main and assign to me").
```

Wait for user reply before proceeding.

**If argument given** → parse it:
- Natural language → infer the target field(s) and value(s)
- Explicit flags → use them directly

### Step 3: Validate values

- **Target branch**: must exist in remote branches listed above. If not found, list available and abort.
- **Assignee / reviewer**: pass through to glab (it validates).

### Step 4: Execute

Run a single `glab mr update` with all changes combined.
Do NOT touch title or description (that's `/mr-beautify`'s job).

### Step 5: Report before/after diff of changed fields.

## Supported fields

| Field | Flag form | Natural language examples |
|-------|-----------|---------------------------|
| Target branch | `--target <branch>` | "target main", "target dev" |
| Assignee | `--assignee <user>` | "assign to me", "assign to alice" |
| Reviewer | `--reviewer <user>` | "reviewers bob and carol" |
| Add labels | `--label <labels>` | "add urgent label" |
| Remove labels | `--unlabel <labels>` | "remove wip label" |
| Draft status | `--draft` / `--ready` | "mark draft", "mark ready" |
| Milestone | `--milestone <name>` | "set milestone to v2.0" |

Use `@me` to refer to the current user.

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

- **No MR**: suggest installing `git-workflow` or creating one with
  `glab mr create`
- **No flags**: print usage table
- **Invalid target branch**: list available remote branches
- **glab failure**: surface error verbatim, do not retry

When a request is present and unambiguous, execute the update and report it in
one response. Interactive mode must stop after showing the menu and wait for the
user's reply.
