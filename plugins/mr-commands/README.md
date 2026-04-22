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
/mr-update [request]
```

Update MR metadata (target branch, assignee, reviewer, labels, draft, milestone). Title/description are handled by `/mr-beautify`.

**Interactive** — run with no argument to see current state and a menu:

```bash
/mr-update
```

**Natural language** — just say what you want:

```bash
/mr-update 改成 main 分支
/mr-update 指派给我，加 urgent 标签
/mr-update mark ready
```

**Explicit flags** (power users): `--target`, `--assignee`, `--reviewer`, `--label`, `--unlabel`, `--draft`, `--ready`, `--milestone`.

### /mr-list

```bash
/mr-list [--all]
```

Lists open MRs. Without `--all`, shows only your own MRs.

## Troubleshooting

- `glab: command not found` → `brew install glab`
- Auth error → `glab auth login`
- No MRs shown → check for open MRs or use `--all`
