from __future__ import annotations

import argparse
import contextlib
import importlib.util
import io
import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "plugins" / "weekly-report" / "scripts" / "collect_weekly_commits.py"
SPEC = importlib.util.spec_from_file_location("collect_weekly_commits", SCRIPT)
assert SPEC and SPEC.loader
collector = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(collector)


def period_args(**overrides: object) -> argparse.Namespace:
    values = {"date": None, "week": None, "since": None, "until": None}
    values.update(overrides)
    return argparse.Namespace(**values)


class PeriodResolutionTest(unittest.TestCase):
    def test_anchor_date_resolves_monday_to_sunday(self) -> None:
        start, end, mode = collector.resolve_period(period_args(date="2026-09-18"))
        self.assertEqual(("2026-09-14", "2026-09-20", "anchor-week"), (str(start), str(end), mode))

    def test_iso_week_resolves_expected_range(self) -> None:
        start, end, mode = collector.resolve_period(period_args(week="2026-W37"))
        self.assertEqual(("2026-09-07", "2026-09-13", "week"), (str(start), str(end), mode))

    def test_overlapping_date_modes_fail(self) -> None:
        with contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit):
                collector.resolve_period(period_args(date="2026-09-18", week="2026-W37"))


class CollectorIntegrationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.repo = Path(self.temp.name) / "repo"
        self.repo.mkdir()
        self.git("init")
        self.git("config", "user.name", "Alice")
        self.git("config", "user.email", "alice@example.com")

    def tearDown(self) -> None:
        self.temp.cleanup()

    def git(self, *args: str, env: dict[str, str] | None = None) -> str:
        result = subprocess.run(
            ["git", "-C", str(self.repo), *args],
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=env,
        )
        return result.stdout

    def commit(self, subject: str, day: str, author: str = "alice@example.com") -> None:
        path = self.repo / "work.txt"
        previous = path.read_text(encoding="utf-8") if path.exists() else ""
        path.write_text(previous + subject + "\n", encoding="utf-8")
        self.git("add", "work.txt")
        env = os.environ.copy()
        env.update(
            {
                "GIT_AUTHOR_DATE": f"{day}T12:00:00+00:00",
                "GIT_COMMITTER_DATE": f"{day}T12:00:00+00:00",
                "GIT_AUTHOR_NAME": author.split("@")[0],
                "GIT_AUTHOR_EMAIL": author,
            }
        )
        self.git("commit", "-m", subject, env=env)

    def collect(self, *args: str, env: dict[str, str] | None = None) -> dict[str, object]:
        result = subprocess.run(
            ["python3", str(SCRIPT), "--repo", str(self.repo), *args],
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=env,
        )
        return json.loads(result.stdout)

    def test_author_filter_uses_repository_identity(self) -> None:
        self.commit("feat: alice work", "2026-09-08")
        self.commit("fix: bob work", "2026-09-09", "bob@example.com")
        payload = self.collect("--since", "2026-09-07", "--until", "2026-09-13")
        commits = payload["commits"]
        self.assertEqual(1, payload["commit_count"])
        self.assertEqual("feat: alice work", commits[0]["subject"])

    def test_truncation_keeps_most_recent_commits_in_order(self) -> None:
        for index, day in enumerate(("2026-09-08", "2026-09-09", "2026-09-10"), 1):
            self.commit(f"chore: work {index}", day)
        payload = self.collect(
            "--since", "2026-09-07", "--until", "2026-09-13", "--max-commits", "2"
        )
        self.assertTrue(payload["truncated"])
        self.assertEqual(
            ["chore: work 2", "chore: work 3"],
            [commit["subject"] for commit in payload["commits"]],
        )

    def test_all_authors_returns_every_matching_commit(self) -> None:
        self.commit("feat: alice work", "2026-09-08")
        self.commit("fix: bob work", "2026-09-09", "bob@example.com")
        payload = self.collect(
            "--since", "2026-09-07", "--until", "2026-09-13", "--all-authors"
        )
        self.assertEqual(2, payload["commit_count"])


if __name__ == "__main__":
    unittest.main()
