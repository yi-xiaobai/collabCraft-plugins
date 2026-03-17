---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git diff:*), Bash(git push:*), Bash(git fetch:*), Bash(git pull:*), Bash(git branch:*)
description: Commit and push to remote
---

## Context

- Current git status: !`git status`
- Current git diff (staged and unstaged changes): !`git diff HEAD`
- Current branch: !`git branch --show-current`
- Recent commits: !`git log --oneline -5`

## Your task

Based on the above changes, commit and push to remote.

1. Analyze the changes and generate a commit message using Conventional Commits format:
   - `feat`: New feature
   - `fix`: Bug fix
   - `docs`: Documentation
   - `style`: Code style
   - `refactor`: Refactoring
   - `chore`: Build/tools

2. Stage relevant files (avoid .env, credentials, secrets)

3. Create the commit

4. Push to remote origin

You have the capability to call multiple tools in a single response. Stage, commit, and push in a single message. Do not use any other tools or do anything else. Do not send any other text or messages besides these tool calls.
