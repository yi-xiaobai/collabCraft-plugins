---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git diff:*)
description: Create a git commit with auto-generated message
---

## Context

- Current git status: !`git status`
- Current git diff (staged and unstaged changes): !`git diff HEAD --`
- Current branch: !`git branch --show-current`
- Recent commits: !`git log --oneline -10 2>/dev/null || echo "No commits yet"`

## Your task

Based on the above changes, create a single git commit.

1. Stage **all** changed and new files shown in the git status above. Trust the project's `.gitignore` to determine what to exclude — do not apply your own judgment about which files to skip. If `.gitignore` does not exist or does not cover sensitive files (`.env`, credentials, etc.), skip those explicitly.
2. **Delegate message generation to the `commit-message-writer` subagent**
   - The subagent reads the staged diff and returns a Conventional Commits message
   - Do NOT inline message rules here — trust the subagent's output
3. Create the commit with the returned message

You MUST do all of the above in a single message.

## Error Handling

- NEVER use `--no-verify` or `--force`
- If pre-commit check fails, **delegate recovery to the `pre-commit-handler` subagent**
  - Pass the hook failure output
  - On `RETRY`: commit again; repeat until success or `STOP`
  - On `STOP`: report the hook failure to the user — do not attempt fixes (never bump baselines/thresholds); user resolves manually
  - Do NOT inline recovery rules here — trust the subagent's output
