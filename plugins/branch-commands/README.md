# Branch Commands

Git branch workflow commands: create, switch, and merge branches.

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

### /branch-merge

```bash
/branch-merge <source_branch> [--no-ff] [--squash]
```

Merge a branch into current branch with auto-update and conflict resolution.

| Param | Description | Default |
|-------|-------------|---------|
| `source_branch` | Branch to merge | required |
| `--no-ff` | Force merge commit | off |
| `--squash` | Squash commits | off |

```bash
/branch-merge feat-login     # merge feat-login into current
/branch-merge dev --no-ff    # merge dev with merge commit
/branch-merge feat --squash  # squash merge
```

