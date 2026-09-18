from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


class DualMarketplaceTest(unittest.TestCase):
    def test_marketplaces_publish_the_same_plugins(self) -> None:
        claude = load(ROOT / ".claude-plugin" / "marketplace.json")
        codex = load(ROOT / ".agents" / "plugins" / "marketplace.json")
        claude_names = {entry["name"] for entry in claude["plugins"]}
        codex_names = {entry["name"] for entry in codex["plugins"]}
        self.assertEqual(claude_names, codex_names)

    def test_every_plugin_has_matching_manifests_and_shared_skills(self) -> None:
        for plugin in (ROOT / "plugins").iterdir():
            if not plugin.is_dir():
                continue
            with self.subTest(plugin=plugin.name):
                claude = load(plugin / ".claude-plugin" / "plugin.json")
                codex = load(plugin / ".codex-plugin" / "plugin.json")
                self.assertEqual(plugin.name, claude["name"])
                self.assertEqual(plugin.name, codex["name"])
                self.assertEqual(claude["version"], codex["version"])
                self.assertTrue((plugin / codex["skills"]).is_dir())

    def test_codex_marketplace_entries_have_required_policy(self) -> None:
        codex = load(ROOT / ".agents" / "plugins" / "marketplace.json")
        for entry in codex["plugins"]:
            with self.subTest(plugin=entry["name"]):
                self.assertIn(entry["policy"]["installation"], {"AVAILABLE", "INSTALLED_BY_DEFAULT", "NOT_AVAILABLE"})
                self.assertIn(entry["policy"]["authentication"], {"ON_INSTALL", "ON_USE"})
                self.assertTrue(entry["category"])


if __name__ == "__main__":
    unittest.main()
