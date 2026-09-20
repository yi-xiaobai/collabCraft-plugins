# Git Workflow Skill

A Codex-first repository containing one self-contained Skill for the complete
Git lifecycle. The Skill carries team constraints, conflict precedence,
exceptions, failure recovery, provider behavior, and publication criteria;
native model capabilities perform the Git mechanics.

## Structure

```text
.
├── .agents/plugins/marketplace.json
├── .codex-plugin/plugin.json
├── .claude-plugin/plugin.json
├── .github/workflows/validate.yml
├── evals/
├── scripts/
├── skills/git-workflow/SKILL.md
└── tests/
```

There are no nested plugin packages, slash commands, or specialist agents. GitHub
and GitLab behavior lives in the same Skill so Codex has one source of truth.

## Install in Codex

```bash
codex plugin marketplace add ./.agents/plugins
codex plugin add git-workflow@collabcraft-plugins
```

Start a new Codex thread after installation so the Skill is discovered.

## Validate

```bash
python3 scripts/git_context.py
python3 scripts/release_gate.py
```

The release gate verifies the single-Skill structure, Codex distribution,
failure-driven scenario catalog, and automated tests. Passing deterministic
checks is necessary but not sufficient: model scenarios must also beat baseline
without a blocking safety finding before publication.
