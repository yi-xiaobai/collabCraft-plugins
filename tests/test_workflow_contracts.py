from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class WorkflowContractTest(unittest.TestCase):
    def read(self, relative: str) -> str:
        return (ROOT / relative).read_text(encoding="utf-8")

    def test_mr_beautify_requires_confirmation_before_remote_update(self) -> None:
        command = self.read("plugins/gitlab-mr/commands/mr-beautify.md")
        normalized = " ".join(command.split())
        self.assertIn("Ask for confirmation before changing the remote MR", normalized)
        self.assertIn("Only after the user explicitly confirms", command)
        self.assertNotIn("single message", command)

    def test_interactive_commands_explicitly_wait(self) -> None:
        for relative in (
            "plugins/dependency-upgrade/commands/turtle-upgrade.md",
            "plugins/gitlab-mr/commands/mr-update.md",
        ):
            with self.subTest(relative=relative):
                self.assertIn("wait for", self.read(relative).lower())

    def test_single_use_mr_agent_is_removed(self) -> None:
        agent = ROOT / "plugins" / "gitlab-mr" / "agents" / "mr-summarizer.md"
        self.assertFalse(agent.exists())


if __name__ == "__main__":
    unittest.main()
