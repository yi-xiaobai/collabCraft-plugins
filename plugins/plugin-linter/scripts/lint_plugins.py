#!/usr/bin/env python3
"""Validate CollabCraft plugin files and repository-level consistency."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path


CJK_PATTERN = re.compile(r"[\u4e00-\u9fff]")
COMMAND_REFERENCE = re.compile(
    r"`/([a-z][a-z0-9-]+)|^\s*/([a-z][a-z0-9-]+)\b", re.MULTILINE
)


@dataclass(frozen=True)
class Finding:
    level: str
    path: Path
    message: str


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text
    try:
        closing = next(
            index for index, line in enumerate(lines[1:], 1) if line.strip() == "---"
        )
    except StopIteration:
        return {}, text

    metadata: dict[str, str] = {}
    for line in lines[1:closing]:
        match = re.match(r"^([A-Za-z][A-Za-z0-9_-]*):\s*(.*)$", line)
        if match:
            metadata[match.group(1)] = match.group(2).strip().strip("'\"")
    return metadata, "\n".join(lines[closing + 1 :])


def classify(path: Path) -> str | None:
    if "commands" in path.parts and path.suffix == ".md":
        return "command"
    if "agents" in path.parts and path.suffix == ".md":
        return "agent"
    if path.name == "SKILL.md" and "skills" in path.parts:
        return "skill"
    return None


def lint_common(path: Path, metadata: dict[str, str], body: str) -> list[Finding]:
    findings: list[Finding] = []
    raw = path.read_text(encoding="utf-8")
    if not metadata:
        findings.append(Finding("error", path, "missing or malformed YAML frontmatter"))
    if not metadata.get("description"):
        findings.append(Finding("error", path, "frontmatter requires description"))
    if CJK_PATTERN.search(raw):
        findings.append(
            Finding("error", path, "contains Chinese characters; plugin files must be English")
        )
    if not body.strip():
        findings.append(Finding("error", path, "body is empty"))
    return findings


def lint_command(path: Path, metadata: dict[str, str], body: str) -> list[Finding]:
    findings = lint_common(path, metadata, body)
    tools = metadata.get("allowed-tools", "")
    if not tools:
        findings.append(Finding("error", path, "frontmatter requires allowed-tools"))
    if re.search(r"(?:^|,\s*)Bash(?:\s*,|$)", tools):
        findings.append(Finding("error", path, "generic Bash permission is not allowed"))
    if not re.search(r"^## Context\s*$", body, re.MULTILINE):
        findings.append(Finding("warning", path, "missing ## Context section"))
    if not re.search(r"^## (?:Your )?[Tt]ask\s*$", body, re.MULTILINE):
        findings.append(Finding("error", path, "missing ## Task or ## Your task section"))

    has_single_response = "single message" in body.lower() or "one response" in body.lower()
    has_pause = bool(
        re.search(
            r"wait for the user|ask for confirmation|after the user explicitly confirms|then stop",
            body,
            re.IGNORECASE,
        )
    )
    if not has_single_response and not has_pause:
        findings.append(
            Finding("warning", path, "missing one-response or user-confirmation boundary")
        )
    return findings


def lint_agent(path: Path, metadata: dict[str, str], body: str) -> list[Finding]:
    findings = lint_common(path, metadata, body)
    name = metadata.get("name")
    if not name:
        findings.append(Finding("error", path, "frontmatter requires name"))
    elif name != path.stem:
        findings.append(Finding("warning", path, f"name '{name}' does not match filename"))
    tools = metadata.get("tools")
    if not tools:
        findings.append(Finding("warning", path, "agent inherits all tools"))
    elif re.search(r"(?:^|,\s*)Bash(?:\s*,|$)", tools):
        findings.append(Finding("error", path, "generic Bash permission is not allowed"))
    return findings


def lint_skill(path: Path, metadata: dict[str, str], body: str) -> list[Finding]:
    findings = lint_common(path, metadata, body)
    name = metadata.get("name")
    if not name:
        findings.append(Finding("error", path, "frontmatter requires name"))
    elif name != path.parent.name:
        findings.append(Finding("warning", path, f"name '{name}' does not match skill directory"))
    description = metadata.get("description", "").lower()
    if description and not any(word in description for word in ("when", "use for", "use to")):
        findings.append(
            Finding("warning", path, "description should state when the skill applies")
        )
    return findings


def markdown_files(root: Path, explicit: list[str]) -> list[Path]:
    if explicit:
        result: list[Path] = []
        for value in explicit:
            candidate = Path(value).expanduser()
            if not candidate.is_absolute():
                candidate = root / candidate
            if candidate.is_dir():
                result.extend(candidate.rglob("*.md"))
            elif candidate.is_file():
                result.append(candidate)
        return sorted({path.resolve() for path in result if classify(path)})

    patterns = (
        "plugins/*/commands/*.md",
        "plugins/*/agents/*.md",
        "plugins/*/skills/*/SKILL.md",
    )
    return sorted(path for pattern in patterns for path in root.glob(pattern))


def read_json(path: Path, findings: list[Finding]) -> object | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        findings.append(Finding("error", path, f"invalid JSON: {error}"))
        return None


def documented_commands(readme: str) -> set[str]:
    return {left or right for left, right in COMMAND_REFERENCE.findall(readme)}


def lint_repository(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    marketplace_path = root / ".claude-plugin" / "marketplace.json"
    codex_marketplace_path = root / ".agents" / "plugins" / "marketplace.json"
    plugins_root = root / "plugins"
    if not marketplace_path.exists() or not plugins_root.is_dir():
        return findings

    marketplace = read_json(marketplace_path, findings)
    if not isinstance(marketplace, dict):
        return findings
    entries = marketplace.get("plugins")
    if not isinstance(entries, list):
        findings.append(Finding("error", marketplace_path, "plugins must be an array"))
        return findings

    marketplace_names: set[str] = set()
    for entry in entries:
        if not isinstance(entry, dict):
            findings.append(Finding("error", marketplace_path, "plugin entry must be an object"))
            continue
        name = entry.get("name")
        source = entry.get("source")
        if not isinstance(name, str) or not name:
            findings.append(Finding("error", marketplace_path, "plugin entry requires name"))
            continue
        if name in marketplace_names:
            findings.append(Finding("error", marketplace_path, f"duplicate plugin '{name}'"))
        marketplace_names.add(name)
        if isinstance(source, dict):
            source = source.get("path")
        if not isinstance(source, str):
            findings.append(Finding("error", marketplace_path, f"'{name}' requires source path"))
            continue

        plugin_path = (root / source).resolve()
        manifest_path = plugin_path / ".claude-plugin" / "plugin.json"
        if not plugin_path.is_dir():
            findings.append(Finding("error", marketplace_path, f"source for '{name}' is missing"))
            continue
        if not manifest_path.exists():
            findings.append(Finding("error", manifest_path, f"'{name}' has no Claude manifest"))
            continue
        manifest = read_json(manifest_path, findings)
        if isinstance(manifest, dict) and manifest.get("name") != name:
            findings.append(Finding("error", manifest_path, f"manifest name must be '{name}'"))

    codex_marketplace_names: set[str] = set()
    if codex_marketplace_path.exists():
        codex_marketplace = read_json(codex_marketplace_path, findings)
        codex_entries = codex_marketplace.get("plugins") if isinstance(codex_marketplace, dict) else None
        if not isinstance(codex_entries, list):
            findings.append(Finding("error", codex_marketplace_path, "plugins must be an array"))
        else:
            for entry in codex_entries:
                if not isinstance(entry, dict):
                    findings.append(Finding("error", codex_marketplace_path, "plugin entry must be an object"))
                    continue
                name = entry.get("name")
                source = entry.get("source")
                source_path = source.get("path") if isinstance(source, dict) else None
                if not isinstance(name, str) or not name:
                    findings.append(Finding("error", codex_marketplace_path, "plugin entry requires name"))
                    continue
                if name in codex_marketplace_names:
                    findings.append(Finding("error", codex_marketplace_path, f"duplicate plugin '{name}'"))
                codex_marketplace_names.add(name)
                if not isinstance(source_path, str):
                    findings.append(Finding("error", codex_marketplace_path, f"'{name}' requires local source.path"))
                    continue
                codex_manifest = (root / source_path / ".codex-plugin" / "plugin.json").resolve()
                if not codex_manifest.exists():
                    findings.append(Finding("error", codex_manifest, f"'{name}' has no Codex manifest"))
                policy = entry.get("policy")
                if not isinstance(policy, dict) or not policy.get("installation") or not policy.get("authentication"):
                    findings.append(Finding("error", codex_marketplace_path, f"'{name}' requires installation and authentication policy"))
                if not isinstance(entry.get("category"), str):
                    findings.append(Finding("error", codex_marketplace_path, f"'{name}' requires category"))

    manifest_names: set[str] = set()
    codex_manifest_names: set[str] = set()
    for plugin_path in sorted(path for path in plugins_root.iterdir() if path.is_dir()):
        manifest_path = plugin_path / ".claude-plugin" / "plugin.json"
        if not manifest_path.exists():
            findings.append(Finding("error", manifest_path, "plugin has no Claude manifest"))
            continue
        manifest = read_json(manifest_path, findings)
        if isinstance(manifest, dict):
            name = manifest.get("name")
            if name != plugin_path.name:
                findings.append(Finding("error", manifest_path, "name must match directory"))
            if isinstance(name, str):
                manifest_names.add(name)

        if codex_marketplace_path.exists():
            codex_manifest_path = plugin_path / ".codex-plugin" / "plugin.json"
            if not codex_manifest_path.exists():
                findings.append(Finding("error", codex_manifest_path, "plugin has no Codex manifest"))
            else:
                codex_manifest = read_json(codex_manifest_path, findings)
                if isinstance(codex_manifest, dict):
                    codex_name = codex_manifest.get("name")
                    if codex_name != plugin_path.name:
                        findings.append(Finding("error", codex_manifest_path, "name must match directory"))
                    if isinstance(codex_name, str):
                        codex_manifest_names.add(codex_name)
                    if isinstance(manifest, dict) and codex_manifest.get("version") != manifest.get("version"):
                        findings.append(Finding("error", codex_manifest_path, "Claude and Codex versions must match"))
                    skills_path = codex_manifest.get("skills")
                    if not isinstance(skills_path, str) or not (plugin_path / skills_path).is_dir():
                        findings.append(Finding("error", codex_manifest_path, "skills must point to an existing directory"))

        commands_dir = plugin_path / "commands"
        actual = {path.stem for path in commands_dir.glob("*.md")} if commands_dir.exists() else set()
        readme_path = plugin_path / "README.md"
        if readme_path.exists():
            documented = documented_commands(readme_path.read_text(encoding="utf-8"))
            for command in sorted(actual - documented):
                findings.append(Finding("error", readme_path, f"'/{command}' is undocumented"))
            for command in sorted(documented - actual):
                findings.append(Finding("error", readme_path, f"'/{command}' has no command file"))

        for agent_path in plugin_path.glob("agents/*.md"):
            references = sum(
                candidate.read_text(encoding="utf-8").count(agent_path.stem)
                for candidate in plugin_path.rglob("*.md")
                if candidate != agent_path
            )
            if references < 2:
                findings.append(
                    Finding("warning", agent_path, "agent is not reused by two entry points")
                )

    for name in sorted(manifest_names - marketplace_names):
        findings.append(Finding("error", marketplace_path, f"'{name}' is absent from marketplace"))
    if codex_marketplace_path.exists():
        for name in sorted(codex_manifest_names - codex_marketplace_names):
            findings.append(Finding("error", codex_marketplace_path, f"'{name}' is absent from Codex marketplace"))
        if marketplace_names != codex_marketplace_names:
            findings.append(Finding("error", codex_marketplace_path, "Claude and Codex marketplace inventories differ"))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", help="optional files or directories")
    parser.add_argument("--root", default=".", help="plugin repository root")
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    findings: list[Finding] = []
    files = markdown_files(root, args.paths)
    for path in files:
        metadata, body = parse_frontmatter(path)
        kind = classify(path)
        if kind == "command":
            findings.extend(lint_command(path, metadata, body))
        elif kind == "agent":
            findings.extend(lint_agent(path, metadata, body))
        elif kind == "skill":
            findings.extend(lint_skill(path, metadata, body))

    if not args.paths:
        findings.extend(lint_repository(root))

    errors = sum(finding.level == "error" for finding in findings)
    warnings = sum(finding.level == "warning" for finding in findings)
    print("Plugin lint report")
    print(f"Scanned {len(files)} plugin file(s)")
    for finding in findings:
        try:
            display_path = finding.path.resolve().relative_to(root)
        except ValueError:
            display_path = finding.path
        print(f"{finding.level.upper()}: {display_path}: {finding.message}")
    print(f"Summary: {errors} error(s), {warnings} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
