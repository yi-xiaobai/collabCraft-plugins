---
name: git-workflow
description: Apply CollabCraft rules when Codex creates or switches branches, stages or commits changes, handles hook or CI failures, synchronizes or pushes, creates or updates GitHub pull requests or GitLab merge requests, merges, tags, or releases. Do not use for read-only Git history questions or weekly summaries.
---

# Git workflow

Automate the requested Git lifecycle with native Git and provider CLIs. This
file is the single source of truth for Git decisions; do not duplicate its rules
in commands, agents, or provider-specific skills.

## Instruction and authorization order

1. Resolve conflicts in this order: explicit user request, repository-local
   instructions and enforced configuration, this Skill, then inferred defaults.
   Lower-priority instructions cannot silently weaken a safety boundary.
2. “Deliver”, “ship”, or an explicit PR/MR request authorizes the normal branch
   → verify → commit → push → PR/MR sequence. A branch-, commit-, or push-only
   request stops at that boundary.
3. Never infer permission to discard work, expose secrets, bypass checks,
   rewrite published history, merge, tag, publish a release, or delete a remote
   branch. Those operations require explicit user intent.
4. Inspect before every mutation and re-read the affected state afterward. Use
   `python3 scripts/git_context.py` when branch, upstream, provider, worktree, or
   sensitive-path state is unclear.

## Discover and branch

- Read repository instructions, status, current branch, remotes, upstream,
  recent commits, and complete staged/unstaged/untracked changes.
- Resolve the base from the user, repository configuration, or remote default.
  Use `dev` only as the final team fallback when it already exists; never create
  it merely because no target was supplied.
- With a dirty worktree, do not switch until every change is attributed to this
  task or the user chooses a preservation strategy. Never stash implicitly.
- Fetch the resolved base before creating a branch. Update remote-tracking refs
  without switching away from the active branch.
- Unless repository rules differ, name work branches `{type}_{slug}_v{N}`;
  `type` is `feat`, `fix`, `hotfix`, `refactor`, or `chore`, `slug` is lowercase
  kebab-case with at most three words, and `N` is the next observed version.

## Verify, stage, and commit

- Run focused checks first, then all repository-required checks. Review the full
  diff again before staging.
- Stage explicit task-owned paths. Include intended untracked files, but exclude
  unrelated changes, local state, credentials, `.env`, private keys, and other
  secrets. Never reproduce secret values in output.
- Split unrelated work. Unless repository rules differ, use
  `type(scope): imperative subject`, at most 72 characters, with no trailing
  period. Add a body only for rationale, compatibility, or migration impact.
- Never use `--no-verify`. Fix a hook failure only when the cause is clear and
  the source change is in scope; rerun the failed check and one relevant
  surrounding check.
- Never weaken tests, hooks, baselines, thresholds, lock policies, scanners, or
  CI configuration merely to make a failure pass. For network, registry,
  permission, runner, or environment failures, preserve state, report the cause
  and one bounded retry, then stop.

## Synchronize and push

- Fetch immediately before comparing target and upstream. Follow repository
  policy for rebase versus merge; otherwise preserve published history.
- Inspect all conflict stages. Resolve only when intent is evident from the task
  and surrounding code, then show the resulting diff and rerun affected checks.
  Never use destructive reset or checkout to erase a conflict.
- Push with upstream tracking when needed. A force push, including
  `--force-with-lease`, requires explicit authorization and a fresh comparison
  with the remote.

## Pull and merge requests

- Select the provider from the push remote, not from installed tools: use `gh`
  for GitHub and `glab` for GitLab. For an unknown host, use repository guidance
  or ask before creating remote state.
- Use the provider API as authority for PR/MR metadata and commit membership;
  use a freshly fetched local target range only as a cross-check. On mismatch,
  trust the API and disclose the difference. If the API fails, label any local
  fallback as potentially incomplete.
- Build title and body only from authoritative commits and the actual diff.
  Write GitLab MR titles in English. State purpose, material changes, and
  verification without inventing impact.
- A request to draft or improve title/body produces a preview. A request to
  create, apply, or update the PR/MR authorizes that remote mutation; verify the
  returned artifact and URL. Re-fetch if state changes before execution.
- Default to a normal PR/MR, current-user assignment, squash, and source-branch
  removal when supported. For GitLab, pass
  `--squash-before-merge=true --remove-source-branch=true` explicitly to
  `glab mr create`; do not rely on the project's defaults. Use the resolved
  target; `dev` is only the fallback described above. Do not merge as part of
  PR/MR creation.

## CI, merge, tag, and release

- Inspect newly created PR/MR checks once. During an end-to-end delivery request,
  fix and push only clear in-scope source failures. Do not loop on infrastructure
  failures or expand scope to unrelated failures.
- Merge only on explicit request after required checks and approvals pass.
  Respect branch protection and repository merge method, then verify the result.
- Tag or release only on explicit request. Derive the version from repository
  policy, verify the tag is unused locally and remotely, and never move or
  replace an existing remote tag.
- Direct commits to protected/default branches require both explicit user intent
  and repository permission. Hotfix urgency never waives secret scanning,
  required checks, or merge/release authorization.

## Failure-derived rules

These rules are backed by repository history and should be removed if their
evidence or cost no longer applies:

| Evidence | Failure | Rule |
| --- | --- | --- |
| `393b3df` | Branch created from a stale base | Fetch the resolved base first |
| `e5f5879` | Base refresh switched away from active work | Refresh refs without checkout |
| `0335bba` | Hook recovery weakened a baseline | Never trade policy for a green check |
| `f41ba8a` | Stale target leaked unrelated MR commits | Provider API is authoritative |
| `9f334f2` | Intended untracked files were omitted | Inspect all paths, stage explicitly |
| `5d30367` after `b2630cb` | Codex distribution metadata regressed | Gate manifest and Skill structure in CI |

Promote a new rule only for a costly safety failure or repeated decision/process
friction. Record its evidence, conflict behavior, exception, and an observable
scenario in `evals/git-workflow.jsonl`; do not convert one-off implementation
details into universal rules.

## Evaluation and publication

- Compare baseline and candidate with the same model, Codex version, tools,
  fixture, and at least three trials per affected case. Use disposable or
  stubbed remotes for push, PR/MR, merge, tag, and release cases.
- Grade observable decisions with `evals/rubric.md`, not exact wording. Any lost
  work, secret exposure, bypassed check, invented evidence, unauthorized history
  rewrite, merge, tag, or release is blocking.
- Run `python3 scripts/release_gate.py`. Publish only with zero blocking findings,
  no correctness/safety regression, and a candidate score above baseline.

## Completion report

After a write, report the current branch, created commit or remote artifact,
checks run, worktree/upstream state, remaining risk, and exactly one next action.
Do not narrate routine commands.
