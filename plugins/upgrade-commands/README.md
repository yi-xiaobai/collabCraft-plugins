# Upgrade Commands

Automates dependency upgrades and creates an MR.

## Commands

| Command | Description |
|---------|-------------|
| `/turtle-upgrade [version]` | Upgrade `@master/turtle` to the specified version |

```bash
/turtle-upgrade 2.1.0                          # from dev → MR to dev
/turtle-upgrade 2.1.0 --from master            # from master → MR to dev
/turtle-upgrade 2.1.0 --from master --to master  # from master → MR to master
```

Creates branch `chore_upgrade_turtle_<version>`, upgrades the package, commits, and opens an MR.

## Requirements

- `glab` CLI installed and authenticated
- `pnpm` package manager
