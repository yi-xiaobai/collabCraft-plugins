#!/bin/sh
set -eu

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
repo_root=$(CDPATH= cd -- "$script_dir/.." && pwd)

exec python3 "$repo_root/plugins/plugin-linter/scripts/lint_plugins.py" \
  --root "$repo_root" "$@"
