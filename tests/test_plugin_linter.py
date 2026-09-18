from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "plugins" / "plugin-linter" / "scripts" / "lint_plugins.py"


class PluginLinterTest(unittest.TestCase):
    def run_lint(self, root: Path, *paths: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["python3", str(SCRIPT), "--root", str(root), *paths],
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

    def test_cjk_is_rejected_without_gnu_grep(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            command = root / "plugins" / "demo" / "commands" / "demo.md"
            command.parent.mkdir(parents=True)
            command.write_text(
                "---\nallowed-tools: Read\ndescription: Demo\n---\n"
                "## Context\n\n中文\n\n## Task\n\nDo it in one response.\n",
                encoding="utf-8",
            )
            result = self.run_lint(root, str(command))
            self.assertEqual(1, result.returncode)
            self.assertIn("contains Chinese characters", result.stdout)

    def test_marketplace_source_requires_manifest(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            marketplace = root / ".claude-plugin" / "marketplace.json"
            marketplace.parent.mkdir(parents=True)
            marketplace.write_text(
                json.dumps(
                    {
                        "name": "demo",
                        "plugins": [
                            {"name": "missing", "source": "./plugins/missing"}
                        ],
                    }
                ),
                encoding="utf-8",
            )
            (root / "plugins" / "missing").mkdir(parents=True)
            result = self.run_lint(root)
            self.assertEqual(1, result.returncode)
            self.assertIn("has no Claude manifest", result.stdout)

    def test_readme_command_drift_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            plugin = root / "plugins" / "demo"
            (plugin / ".claude-plugin").mkdir(parents=True)
            (plugin / "commands").mkdir()
            (root / ".claude-plugin").mkdir()
            (root / ".claude-plugin" / "marketplace.json").write_text(
                json.dumps(
                    {
                        "name": "demo",
                        "plugins": [{"name": "demo", "source": "./plugins/demo"}],
                    }
                ),
                encoding="utf-8",
            )
            (plugin / ".claude-plugin" / "plugin.json").write_text(
                json.dumps({"name": "demo", "description": "Demo", "author": {"name": "Test"}}),
                encoding="utf-8",
            )
            (plugin / "README.md").write_text("Use `/old-command`.\n", encoding="utf-8")
            (plugin / "commands" / "new-command.md").write_text(
                "---\nallowed-tools: Read\ndescription: Demo\n---\n"
                "## Context\n\nNone.\n\n## Task\n\nDo it in one response.\n",
                encoding="utf-8",
            )
            result = self.run_lint(root)
            self.assertEqual(1, result.returncode)
            self.assertIn("'/new-command' is undocumented", result.stdout)
            self.assertIn("'/old-command' has no command file", result.stdout)


if __name__ == "__main__":
    unittest.main()
