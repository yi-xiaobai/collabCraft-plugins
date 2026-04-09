# MR Commands

GitLab Merge Request workflow commands.

## Commands

### /mr-beautify

```bash
/mr-beautify [target-branch]
```

Generates an MR title and description from git commits, then updates the remote MR. Default target: `dev`.

### /mr-list

```bash
/mr-list [--all]
```

Lists open MRs. Without `--all`, shows only your own MRs.

## Troubleshooting

- `glab: command not found` → `brew install glab`
- Auth error → `glab auth login`
- No MRs shown → check for open MRs or use `--all`
