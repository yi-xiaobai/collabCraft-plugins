#!/usr/bin/env python3
"""Collect Git commit evidence for a resolved weekly-report period."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import date, datetime, time, timedelta
from pathlib import Path
from typing import NoReturn


def fail(message: str) -> NoReturn:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(2)


def run_git(repo: Path, *args: str, check: bool = True) -> str:
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if check and result.returncode != 0:
        fail(result.stderr.strip() or f"git {' '.join(args)} failed")
    return result.stdout


def parse_day(value: str, label: str) -> date:
    try:
        return date.fromisoformat(value)
    except ValueError:
        fail(f"{label} must use YYYY-MM-DD")


def resolve_period(args: argparse.Namespace) -> tuple[date, date, str]:
    explicit_range = args.since is not None or args.until is not None
    modes = sum((args.date is not None, args.week is not None, explicit_range))
    if modes > 1:
        fail("use only one date mode: --date, --week, or --since/--until")

    if explicit_range:
        if args.since is None or args.until is None:
            fail("--since and --until must be provided together")
        start = parse_day(args.since, "--since")
        end = parse_day(args.until, "--until")
        mode = "range"
    elif args.week:
        match = re.fullmatch(r"(\d{4})-W(\d{2})", args.week)
        if not match:
            fail("--week must use YYYY-Www, for example 2026-W37")
        try:
            start = date.fromisocalendar(int(match.group(1)), int(match.group(2)), 1)
        except ValueError:
            fail(f"invalid ISO week: {args.week}")
        end = start + timedelta(days=6)
        mode = "week"
    elif args.date:
        anchor = parse_day(args.date, "--date")
        start = anchor - timedelta(days=anchor.weekday())
        end = start + timedelta(days=6)
        mode = "anchor-week"
    else:
        today = date.today()
        this_monday = today - timedelta(days=today.weekday())
        start = this_monday - timedelta(days=7)
        end = this_monday - timedelta(days=1)
        mode = "previous-week"

    if start > end:
        fail("--since cannot be later than --until")
    return start, end, mode


def resolve_author(repo: Path, args: argparse.Namespace) -> tuple[str | None, str]:
    if args.all_authors:
        return None, "all authors"
    if args.author:
        return args.author, args.author

    email = run_git(repo, "config", "user.email", check=False).strip()
    if email:
        return email, email
    name = run_git(repo, "config", "user.name", check=False).strip()
    if name:
        return name, name
    fail("Git identity is not configured; pass --author or --all-authors")


def commit_details(repo: Path, commit_hash: str) -> dict[str, object]:
    raw = run_git(
        repo,
        "show",
        "-s",
        "--format=%H%x1f%aI%x1f%an%x1f%ae%x1f%s%x1f%b",
        commit_hash,
    ).rstrip("\n")
    fields = raw.split("\x1f", 5)
    if len(fields) != 6:
        fail(f"could not parse commit {commit_hash}")

    additions = 0
    deletions = 0
    files: list[str] = []
    numstat = run_git(repo, "show", "--numstat", "--format=", "--no-renames", commit_hash)
    for line in numstat.splitlines():
        parts = line.split("\t", 2)
        if len(parts) != 3:
            continue
        added, deleted, path = parts
        files.append(path)
        if added.isdigit():
            additions += int(added)
        if deleted.isdigit():
            deletions += int(deleted)

    return {
        "hash": fields[0],
        "date": fields[1],
        "author_name": fields[2],
        "author_email": fields[3],
        "subject": fields[4],
        "body": fields[5].strip(),
        "files": files,
        "additions": additions,
        "deletions": deletions,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Collect commit evidence for a weekly work report as JSON."
    )
    parser.add_argument("--repo", default=".", help="Git repository path")
    parser.add_argument("--date", help="anchor date whose Monday-Sunday week is used")
    parser.add_argument("--week", help="ISO week in YYYY-Www form")
    parser.add_argument("--since", help="inclusive range start in YYYY-MM-DD form")
    parser.add_argument("--until", help="inclusive range end in YYYY-MM-DD form")
    author_group = parser.add_mutually_exclusive_group()
    author_group.add_argument("--author", help="Git author pattern")
    author_group.add_argument("--all-authors", action="store_true")
    parser.add_argument("--refs", choices=("all", "current"), default="all")
    parser.add_argument("--max-commits", type=int, default=200)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.max_commits < 1:
        fail("--max-commits must be greater than zero")

    repo_input = Path(args.repo).expanduser()
    root_text = run_git(repo_input, "rev-parse", "--show-toplevel").strip()
    repo = Path(root_text)
    start, end, period_mode = resolve_period(args)
    author_pattern, author_label = resolve_author(repo, args)

    since = datetime.combine(start, time.min).isoformat()
    until_inclusive = datetime.combine(end, time(23, 59, 59)).isoformat()
    rev_args = ["rev-list", "--all" if args.refs == "all" else "HEAD"]
    rev_args.extend(
        [
            "--no-merges",
            "--reverse",
            f"--since={since}",
            f"--until={until_inclusive}",
        ]
    )
    if author_pattern:
        rev_args.append(f"--author={author_pattern}")

    hashes = [line for line in run_git(repo, *rev_args).splitlines() if line]
    truncated = len(hashes) > args.max_commits
    selected = hashes[: args.max_commits]
    commits = [commit_details(repo, commit_hash) for commit_hash in selected]

    payload = {
        "repository": str(repo),
        "period": {
            "start": start.isoformat(),
            "end": end.isoformat(),
            "mode": period_mode,
            "timezone": datetime.now().astimezone().tzname(),
        },
        "filters": {"author": author_label, "refs": args.refs, "merge_commits": False},
        "commit_count": len(commits),
        "truncated": truncated,
        "available_commit_count": len(hashes),
        "commits": commits,
    }
    json.dump(payload, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
