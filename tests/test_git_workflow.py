from __future__ import annotations

import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "git_context.py"


class GitContextTest(unittest.TestCase):
    def git(self, repo: Path, *args: str) -> None:
        subprocess.run(["git", *args], cwd=repo, check=True, capture_output=True, text=True)

    def test_reports_dirty_untracked_sensitive_path_without_content(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            self.git(repo, "init")
            self.git(repo, "config", "user.name", "Test")
            self.git(repo, "config", "user.email", "test@example.com")
            (repo / "README.md").write_text("ok\n", encoding="utf-8")
            self.git(repo, "add", "README.md")
            self.git(repo, "commit", "-m", "docs: initialize")
            (repo / ".env").write_text("TOKEN=do-not-print\n", encoding="utf-8")
            result = subprocess.run(
                ["python3", str(SCRIPT), "--repo", str(repo)],
                check=True,
                capture_output=True,
                text=True,
            )
            self.assertNotIn("do-not-print", result.stdout)
            data = json.loads(result.stdout)
            self.assertTrue(data["dirty"])
            self.assertEqual(data["sensitive_paths"], [".env"])
            self.assertTrue(data["stop_reasons"])

    def test_preserves_worktree_status_columns_for_modified_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            self.git(repo, "init")
            self.git(repo, "config", "user.name", "Test")
            self.git(repo, "config", "user.email", "test@example.com")
            tracked = repo / ".config"
            tracked.write_text("before\n", encoding="utf-8")
            self.git(repo, "add", ".config")
            self.git(repo, "commit", "-m", "chore: initialize")
            tracked.write_text("after\n", encoding="utf-8")
            result = subprocess.run(
                ["python3", str(SCRIPT), "--repo", str(repo)],
                check=True,
                capture_output=True,
                text=True,
            )
            self.assertEqual(json.loads(result.stdout)["changes"], [{"code": " M", "path": ".config"}])


class WorkflowContractTest(unittest.TestCase):
    def test_failure_evidence_commits_exist(self) -> None:
        catalog = (ROOT / "skills/git-workflow/SKILL.md").read_text(encoding="utf-8")
        for commit in ("393b3df", "e5f5879", "0335bba", "f41ba8a", "9f334f2", "5d30367", "b2630cb"):
            self.assertIn(commit, catalog)
            result = subprocess.run(["git", "cat-file", "-e", f"{commit}^{{commit}}"], cwd=ROOT)
            self.assertEqual(result.returncode, 0)

    def test_repository_contains_exactly_one_skill(self) -> None:
        skills = list(ROOT.glob("**/SKILL.md"))
        self.assertEqual(skills, [ROOT / "skills/git-workflow/SKILL.md"])


if __name__ == "__main__":
    unittest.main()
