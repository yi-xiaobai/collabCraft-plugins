---
name: weekly-report
description: Create an evidence-based weekly work summary from Git commits in the current repository. Use when the user asks for a weekly report, last week's work, or a summary for a selected week or date range.
---

# Git Weekly Report

Use the bundled [collector](../../scripts/collect_weekly_commits.py) before
writing the report. Resolve that link relative to this `SKILL.md`; the script
returns commit metadata, changed paths, and line statistics as JSON:

```bash
python3 /resolved/plugin/path/scripts/collect_weekly_commits.py [options]
```

## Period selection

- With no date input, use the previous completed calendar week, Monday through
  Sunday, in the machine's local timezone.
- Treat a bare `YYYY-MM-DD` as an anchor date and summarize its Monday-through-
  Sunday week. Pass it to the collector as `--date`.
- Accept an ISO week as `--week YYYY-Www`.
- Accept an exact inclusive range only when both `--since YYYY-MM-DD` and
  `--until YYYY-MM-DD` are present.
- If the user gives overlapping date modes, ask them to choose one instead of
  silently guessing.

By default, collect commits across all local refs and restrict authorship to the
repository's configured `user.email`, falling back to `user.name`. Respect
`--author`, `--all-authors`, or `--refs current` when requested.

## Evidence rules

- Base every claim on commit subjects, bodies, and changed paths returned by
  the collector. Never invent outcomes, business impact, or completion state.
- Consolidate follow-up fixes and commits touching the same feature into one
  meaningful work item. Describe delivered capabilities rather than replaying
  commit messages or listing files.
- Use changed paths to disambiguate scope, not as content to copy into the
  report.
- Exclude merge commits. If the result is truncated, disclose that the report
  covers only the most recent returned commits.
- If no commits match, state the resolved period and author filter and report
  that no matching work was found. Do not manufacture a summary.

## Output

Follow the user's language; default to Simplified Chinese. Match the compact
style of a professional weekly update:

1. Start with a localized "Last Week Work Summary" heading and show the
   inclusive period using long-form calendar dates.
2. Write a numbered list of three to six grouped work items when the evidence
   supports that many. Fewer items are acceptable.
3. Begin each item with a short theme, followed by a colon and one or two
   concrete sentences describing the completed work.
4. Omit hashes, raw statistics, author details, and file paths unless the user
   asks for evidence or a detailed version.
5. Preserve uncertainty: use wording such as "worked on" or "adjusted" when
   commits do not prove that a feature was fully completed.
