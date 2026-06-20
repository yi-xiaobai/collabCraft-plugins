# Tag Commands

Git tag workflow for debug-pri style tags: list tags grouped by service, and create new tags by bumping version.

## Commands

| Command | Description |
|---------|-------------|
| `/tag-list` | List all debug-pri tags grouped by service name |
| `/tag-new` | Create a new debug-pri tag by bumping version for current user |

## Tag Format

```
debug-pri-<name>-v<semver>
```

- `<name>` is derived from `git config user.name` by taking the first character of each name segment (e.g. `luoyi` → `ly`, `张三` → `zs`)
- `<semver>` follows `vX.Y.Z` convention

## Usage

### List tags

```
/tag-list
/tag-list backend
```

Lists all `debug-pri-*` tags grouped by service name, showing version and commit date.

### Create new tag

```
/tag-new              # bump patch (default)
/tag-new minor        # bump minor
/tag-new major        # bump major
/tag-new v2.0.0       # explicit version
/tag-new --dry-run    # preview only
```

Flow:
1. Reads author name from git config and computes abbreviation
2. Looks up existing tags for this abbreviation
3. Delegates to `tag-pattern-analyzer` to detect pattern and compute next version
4. Shows analysis and asks for confirmation
5. Creates annotated tag: `debug-pri: <abbr> <version>`
6. Pushes to remote
