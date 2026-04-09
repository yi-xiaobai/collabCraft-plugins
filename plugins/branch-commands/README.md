# Branch Commands

Git branch workflow commands: create, switch, and delete branches.

## Commands

### /branch-create

```bash
/branch-create [type] [base_branch] [ide]
```

Creates a new branch with auto-versioned name.

| Param | Values | Default |
|-------|--------|---------|
| `type` | `feat`, `fix`, `hotfix` | required |
| `base_branch` | any branch | `dev` |
| `ide` | `windsurf`, `vscode` | `windsurf` |

```bash
/branch-create feat              # → feat-xxx-v3
/branch-create fix master        # → fix-xxx-v2 from master
```

### /branch-switch

```bash
/branch-switch [keyword]
```

Fuzzy-search and switch branches.

```bash
/branch-switch           # list recent branches
/branch-switch login     # match branches containing "login"
/branch-switch 3         # switch to 3rd in list
```

### /branch-delete

```bash
/branch-delete [option]
```

Clean up merged or stale branches.

```bash
/branch-delete           # show deletable branches
/branch-delete merged    # delete all merged branches
/branch-delete feat-old  # delete specific branch
```

## Safety Rules

- Never deletes: `main`, `master`, `dev`
- Never deletes the current branch
- Remote branch deletion requires confirmation
