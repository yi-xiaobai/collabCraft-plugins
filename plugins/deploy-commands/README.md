# Deploy Commands

Build and publish workflow for Node.js/frontend projects.

## Commands

| Command | Description |
|---------|-------------|
| `/build` | Build the current project |
| `/publish [type]` | Publish to npm registry |
| `/release [type]` | Full flow: build → version → publish → push |

```bash
/publish patch
/publish minor --tag=beta
/release patch
/release minor --dry-run
```

## Version Types

| Type | Example |
|------|---------|
| `patch` | 1.0.0 → 1.0.1 |
| `minor` | 1.0.0 → 1.1.0 |
| `major` | 1.0.0 → 2.0.0 |
| `prerelease` | 1.0.0 → 1.0.1-0 |

## Features

- Auto-detects package manager (npm / yarn / pnpm)
- Auto-detects build script (build / compile / dist)
- Pre-flight checks: clean working tree, correct branch, npm login

## Requirements

- `package.json` in project root
- npm registry configured
- Logged in: `npm login`
