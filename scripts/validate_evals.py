#!/usr/bin/env python3
"""Validate the provider-neutral workflow evaluation catalog."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ALLOWED_RISKS = {"low", "medium", "high"}
REQUIRED_FIELDS = {"id", "plugin", "capability", "risk", "prompt", "criteria", "forbidden"}


def marketplace_plugins(root: Path) -> set[str]:
    path = root / ".claude-plugin" / "marketplace.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    return {entry["name"] for entry in data["plugins"]}


def validate(root: Path, cases_path: Path) -> list[str]:
    errors: list[str] = []
    known_plugins = marketplace_plugins(root)
    seen: set[str] = set()
    count = 0
    has_high_risk = False

    for line_number, raw in enumerate(cases_path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        count += 1
        try:
            case = json.loads(raw)
        except json.JSONDecodeError as error:
            errors.append(f"line {line_number}: invalid JSON: {error}")
            continue
        if not isinstance(case, dict):
            errors.append(f"line {line_number}: case must be an object")
            continue

        missing = REQUIRED_FIELDS - set(case)
        if missing:
            errors.append(f"line {line_number}: missing fields {sorted(missing)}")
        case_id = case.get("id")
        if not isinstance(case_id, str) or not case_id:
            errors.append(f"line {line_number}: id must be a non-empty string")
        elif case_id in seen:
            errors.append(f"line {line_number}: duplicate id '{case_id}'")
        else:
            seen.add(case_id)

        if case.get("plugin") not in known_plugins:
            errors.append(f"line {line_number}: unknown plugin '{case.get('plugin')}'")
        if case.get("risk") not in ALLOWED_RISKS:
            errors.append(f"line {line_number}: invalid risk '{case.get('risk')}'")
        elif case.get("risk") == "high":
            has_high_risk = True
        if not isinstance(case.get("prompt"), str) or not case.get("prompt", "").strip():
            errors.append(f"line {line_number}: prompt must be a non-empty string")
        criteria = case.get("criteria")
        if not isinstance(criteria, list) or not 2 <= len(criteria) <= 5:
            errors.append(f"line {line_number}: criteria must contain 2 to 5 items")
        forbidden = case.get("forbidden")
        if not isinstance(forbidden, list) or not forbidden:
            errors.append(f"line {line_number}: forbidden must contain at least one item")

    if count < 8:
        errors.append("catalog must contain at least 8 cases")
    if not has_high_risk:
        errors.append("catalog must contain at least one high-risk case")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".")
    parser.add_argument("--cases", default="evals/cases.jsonl")
    args = parser.parse_args()
    root = Path(args.root).expanduser().resolve()
    cases_path = Path(args.cases)
    if not cases_path.is_absolute():
        cases_path = root / cases_path

    errors = validate(root, cases_path)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    count = sum(bool(line.strip()) for line in cases_path.read_text(encoding="utf-8").splitlines())
    print(f"Evaluation catalog is valid: {count} case(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
