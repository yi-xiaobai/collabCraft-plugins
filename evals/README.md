# Workflow evaluations

These cases test decisions that are easy to miss in real Git, GitLab, dependency
upgrade, and reporting workflows. They complement deterministic unit tests; they
do not replace them.

## Validate the catalog

```bash
python3 scripts/validate_evals.py
```

Validation is offline and makes no model calls. It checks schema, unique IDs,
known plugin names, risk levels, and evaluation criteria.

## Run an evaluation

Use the same model, tool configuration, repository fixture, and trial count for
the baseline and candidate conditions:

- **baseline**: task prompt without the CollabCraft plugin instructions;
- **candidate**: identical task prompt with the relevant plugin installed;
- at least three trials per case;
- blind the condition names before grading with `rubric.md`;
- record the model, CLI version, tool access, trial count, and failures.

Remote-write cases should use an isolated GitLab test project or a stubbed
`glab`; never run them against a production repository.
