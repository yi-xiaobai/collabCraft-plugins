#!/usr/bin/env python3
"""Collect read-only Git state as JSON without exposing file contents."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
from pathlib import Path


SENSITIVE_NAMES = {".env", ".env.local", ".npmrc", ".pypirc", "credentials.json", "id_rsa", "id_ed25519"}
SENSITIVE_SUFFIXES = {".key", ".pem", ".p12", ".pfx"}


def git(root: Path, *args: str, check: bool = True) -> str:
    result = subprocess.run(["git", *args], cwd=root, text=True, capture_output=True, check=False)
    if check and result.returncode:
        raise RuntimeError(result.stderr.strip() or "git command failed")
    # Porcelain status uses leading spaces as data; never strip the left edge.
    return result.stdout.rstrip()


def redact(url: str) -> str:
    return re.sub(r"(https?://)[^/@]+@", r"\1<redacted>@", url)


def provider(url: str) -> str:
    lowered = url.lower()
    if "github" in lowered:
        return "github"
    if "gitlab" in lowered:
        return "gitlab"
    return "unknown"


def sensitive(path: str) -> bool:
    item = Path(path)
    return item.name in SENSITIVE_NAMES or item.suffix.lower() in SENSITIVE_SUFFIXES


def default_branch(root: Path) -> str | None:
    ref = git(root, "symbolic-ref", "--quiet", "--short", "refs/remotes/origin/HEAD", check=False)
    if ref.startswith("origin/"):
        return ref.removeprefix("origin/")
    refs = set(git(root, "for-each-ref", "--format=%(refname:short)", "refs/heads", "refs/remotes", check=False).splitlines())
    return next((name for name in ("dev", "main", "master") if name in refs or f"origin/{name}" in refs), None)


def collect(path: Path) -> dict[str, object]:
    root = Path(git(path, "rev-parse", "--show-toplevel"))
    changes: list[dict[str, str]] = []
    for line in git(root, "status", "--porcelain=v1", "--untracked-files=all").splitlines():
        if len(line) >= 4:
            changed = line[3:].split(" -> ", 1)[-1]
            changes.append({"code": line[:2], "path": changed})
    branch = git(root, "branch", "--show-current", check=False) or None
    upstream = git(root, "rev-parse", "--abbrev-ref", "@{upstream}", check=False) or None
    ahead = behind = None
    if upstream:
        counts = git(root, "rev-list", "--left-right", "--count", f"{upstream}...HEAD", check=False).split()
        if len(counts) == 2:
            behind, ahead = map(int, counts)
    remotes = []
    for name in git(root, "remote", check=False).splitlines():
        url = git(root, "remote", "get-url", "--push", name, check=False)
        remotes.append({"name": name, "url": redact(url), "provider": provider(url)})
    sensitive_paths = sorted(item["path"] for item in changes if sensitive(item["path"]))
    return {
        "repository": str(root),
        "branch": branch,
        "head": git(root, "rev-parse", "--short", "HEAD", check=False) or None,
        "upstream": upstream,
        "ahead": ahead,
        "behind": behind,
        "default_branch": default_branch(root),
        "dirty": bool(changes),
        "changes": changes,
        "sensitive_paths": sensitive_paths,
        "remotes": remotes,
        "tools": {"gh": bool(shutil.which("gh")), "glab": bool(shutil.which("glab"))},
        "stop_reasons": ["sensitive paths require exclusion and review"] if sensitive_paths else [],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=".")
    args = parser.parse_args()
    try:
        print(json.dumps(collect(Path(args.repo).resolve()), indent=2, ensure_ascii=False))
    except RuntimeError as error:
        print(json.dumps({"error": str(error)}))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
