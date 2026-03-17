---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git diff:*), Bash(git push:*), Bash(git fetch:*), Bash(git branch:*), Bash(git remote:*), Bash(git log:*), Bash(curl:*)
description: Commit, push, and create GitLab Merge Request
---

## Context

- Current git status: !`git status`
- Current git diff (staged and unstaged changes): !`git diff HEAD`
- Current branch: !`git branch --show-current`
- Remote URL: !`git remote get-url origin`
- Recent commits: !`git log --oneline -5`

## Parameters

User may specify target branch: `/commit-push-mr [target_branch]`
- If not specified, default to `dev`
- Common values: `dev`, `master`, `main`, `release/*`

## Your task

Based on the above changes, commit, push, and create a GitLab Merge Request.

1. **Commit changes**
   - Analyze the changes and generate a commit message using Conventional Commits format
   - Stage relevant files (avoid .env, credentials, secrets)
   - Create the commit

2. **Push to remote**
   - Push current branch to origin

3. **Create GitLab MR**
   - Extract project path from remote URL
   - Get project ID from GitLab API
   - Create MR with:
     - Source branch: current branch
     - Target branch: user specified or `dev`
     - Title: commit message
     - Options: delete source branch, squash commits

   ```bash
   # Get project path
   PROJECT_PATH=$(git remote get-url origin | sed 's|.*[:/]\([^/]*/[^/]*\)\.git|\1|')
   ENCODED_PATH=$(echo "$PROJECT_PATH" | sed 's|/|%2F|g')
   
   # Create MR (replace <target_branch> with user input or default 'dev')
   curl -s --request POST \
     --header "PRIVATE-TOKEN: $GITLAB_TOKEN" \
     --header "Content-Type: application/json" \
     --data '{
       "source_branch": "<current_branch>",
       "target_branch": "<target_branch>",
       "title": "<commit_message>",
       "remove_source_branch": true,
       "squash": true
     }' \
     "https://$GITLAB_HOST/api/v4/projects/$ENCODED_PATH/merge_requests"
   ```

4. **Report result**
   - Show MR URL on success

## Configuration

Requires environment variables:
- `GITLAB_TOKEN`: GitLab Personal Access Token
- `GITLAB_HOST`: GitLab domain (e.g., gitlab.company.com)
