---
allowed-tools: Bash(git fetch:*), Bash(git branch:*), Bash(git push:*), Bash(git checkout:*), Bash(open:*), Bash(code:*), Bash(windsurf:*)
description: Create a new Git branch with auto-versioning
---

## Context

- Current git status: !`git status`
- Current branch: !`git branch --show-current`
- Remote branches: !`git branch -r | head -20`
- Existing feature branches: !`git branch -a | grep -E 'feat-|fix-|hotfix-' | tail -10`

## Your task

Create a new Git branch based on user input. Follow these steps:

1. **Parse parameters**
   - Branch type: `feat` (feature), `fix` (bugfix), or `hotfix` (urgent fix)
   - Base branch: default `dev`
   - IDE: default `windsurf`

2. **Generate branch name**
   - Format: `{type}-{description}-v{version}`
   - Get max version from existing branches of same type, increment by 1
   - Translate Chinese description to English kebab-case

3. **Create remote branch first**
   ```bash
   git fetch origin
   git push origin origin/{base_branch}:refs/heads/{new_branch}
   ```

4. **Switch to local branch**
   ```bash
   git fetch origin
   git checkout -b {new_branch} origin/{new_branch}
   ```

5. **Open in IDE** (optional)
   ```bash
   windsurf .  # or: code .
   ```

Report the created branch name when done.
