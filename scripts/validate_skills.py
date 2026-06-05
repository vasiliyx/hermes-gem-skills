#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except Exception:
    yaml = None

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []

for path in sorted((ROOT / "skills").rglob("SKILL.md")):
    rel = path.relative_to(ROOT)
    text = path.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---"):
        errors.append(f"{rel}: must start with YAML frontmatter")
        continue
    m = re.search(r"\n---\s*\n", text[3:])
    if not m:
        errors.append(f"{rel}: missing closing frontmatter delimiter")
        continue
    fm_text = text[3 : m.start() + 3]
    body = text[m.end() + 3 :].strip()
    if not body:
        errors.append(f"{rel}: empty body")
    if yaml is not None:
        try:
            fm = yaml.safe_load(fm_text)
        except Exception as exc:
            errors.append(f"{rel}: invalid YAML: {exc}")
            continue
        if not isinstance(fm, dict):
            errors.append(f"{rel}: frontmatter must be a mapping")
            continue
        for key in ("name", "description"):
            if not fm.get(key):
                errors.append(f"{rel}: missing {key}")
        desc = str(fm.get("description", ""))
        if len(desc) > 1024:
            errors.append(f"{rel}: description > 1024 chars")

if errors:
    print("Skill validation failed:")
    for err in errors:
        print(f"- {err}")
    sys.exit(1)

print("OK: skill validation passed")
