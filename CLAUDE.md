# Repository instructions

All responses and maintained files use English.

This repository distributes exactly one Git workflow Skill:
`skills/git-workflow/SKILL.md`. Keep Git decisions, constraints, conflicts,
exceptions, and failure-derived rules in that file. Do not create nested plugin
packages, command wrappers, or specialist agents for Git behavior.

Use native model capabilities for Git mechanics and deterministic scripts for
state collection, tests, and release gates. Add a Skill rule only from an
observed costly failure or repeated workflow friction, then add an observable
scenario under `evals/`.

Run `python3 scripts/release_gate.py` before publication. Commit messages use
`type(scope): message` unless a higher-priority repository rule changes it.
