# Dependency Upgrade

Automates dependency upgrades and creates an MR.

## Commands

| Command | Description |
|---------|-------------|
| `/turtle-upgrade [version]` | Upgrade `@master/turtle` to the specified version |

```bash
/turtle-upgrade 2.1.0                  # from dev → MR to dev
/turtle-upgrade 2.1.0 --branch master  # from master → MR to master
```

Creates the next versioned `chore_upgrade-turtle_vN` branch, upgrades the
package, commits, and opens an MR targeting the selected base branch.

## Requirements

- `glab` CLI installed and authenticated
- `pnpm` package manager
