# MR Commands

GitLab Merge Request workflow commands.

## Commands

### /mr-beautify

```bash
/mr-beautify [target-branch]
```

Generates an MR title and description from git commits, then updates the remote MR. Default target: `dev`.

### /mr-update

```bash
/mr-update [flags]
```

Update MR metadata without touching title/description.

| Flag | Description |
|------|-------------|
| `--target <branch>` | Change target branch |
| `--assignee <user>` | Set assignee (`@me` for self) |
| `--reviewer <user>` | Set reviewers (comma-separated) |
| `--label <labels>` | Add labels |
| `--unlabel <labels>` | Remove labels |
| `--draft` / `--ready` | Toggle draft status |
| `--milestone <name>` | Set milestone |

```bash
/mr-update --target main
/mr-update --assignee @me --label urgent
/mr-update --draft
/mr-update --target dev --unlabel wip --ready
```

### /mr-list

```bash
/mr-list [--all]
```

Lists open MRs. Without `--all`, shows only your own MRs.

## Troubleshooting

- `glab: command not found` → `brew install glab`
- Auth error → `glab auth login`
- No MRs shown → check for open MRs or use `--all`
