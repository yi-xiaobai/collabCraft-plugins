---
name: gitlab-mr
description: Manage GitLab merge requests with authoritative commit evidence and safe remote updates. Use when listing MRs, improving an MR title or description, or changing MR metadata.
---

# GitLab Merge Requests

Use `glab` for GitLab state. Treat the GitLab merge request API as authoritative
for MR metadata and commit membership.

## List

- List the current user's open MRs by default; include all authors only when the
  user asks.
- Present MR number, title, branch, updated date, and author when relevant.

## Beautify

1. Read the current MR IID and target branch.
2. Fetch its commit list from the GitLab API and cross-check a freshly fetched
   local target diff. Trust the API when they differ and report the mismatch.
3. Generate a Conventional Commits title of at most 72 characters and no more
   description bullets than effective commits after exclusions.
4. Preview the proposed title and description. Update the remote MR only after
   explicit confirmation.
5. Re-fetch the commit list if repository state changes before confirmation.

If the API fails, a freshly fetched local diff may be used as a fallback, but
label the result as potentially incomplete.

## Update metadata

- Support target branch, assignee, reviewer, labels, draft status, and milestone.
- Validate a requested target against remote branches.
- Combine unambiguous requested changes into one update and report a before/after
  diff.
- Do not change title or description during a metadata-only update.
- Stop and surface `glab` errors without blind retries.
