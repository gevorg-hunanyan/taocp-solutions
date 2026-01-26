#!/usr/bin/env python3
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"

text = README.read_text(encoding="utf-8")

# 1) Extract solutions region
m = re.search(
    r"<!--\s*SOLUTIONS_START\s*-->(.*?)(<!--\s*SOLUTIONS_END\s*-->|$)",
    text,
    flags=re.DOTALL,
)
if not m:
    raise SystemExit("Couldn't find <!-- SOLUTIONS_START --> marker in README.md")

region = m.group(1)

# 2) Collect link targets from multiple formats:
targets = []

# (A) Inline Markdown links: [title](target)
targets += re.findall(r"\[[^\]]+\]\(([^)]+)\)", region)

# (B) HTML links: <a href="target">
targets += re.findall(r'<a\s+[^>]*href="([^"]+)"', region, flags=re.IGNORECASE)

# (C) Reference-style links: [title][id]
ref_uses = re.findall(r"\[[^\]]+\]\[([^\]]+)\]", region)

# Reference definitions can be anywhere in README, not necessarily in region:
ref_defs = dict(re.findall(r"^\[([^\]]+)\]:\s*(\S+)\s*$", text, flags=re.MULTILINE))

for ref_id in ref_uses:
    if ref_id in ref_defs:
        targets.append(ref_defs[ref_id])

def is_solution_target(t: str) -> bool:
    t = t.strip()
    # Ignore anchors and mail
    if t.startswith(("#", "mailto:")):
        return False
    # Ignore obvious non-solution noise (badges/images)
    if t.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp")):
        return False
    # Allow both relative paths and repo URLs.
    # If you sometimes link to external gists *as solutions*, remove the http filter below.
    if t.startswith(("http://", "https://")):
        # Count only GitHub links that point into THIS repo (common pattern).
        # This avoids counting random external refs.
        return "github.com" in t.lower()
    return True

count = sum(1 for t in targets if is_solution_target(t))

# 3) Update README counter
new_text, n = re.subn(
    r"(<!--\s*SOLVED_COUNT\s*-->)(.*?)(<!--\s*/SOLVED_COUNT\s*-->)",
    lambda mm: f"{mm.group(1)}{count}{mm.group(3)}",
    text,
    flags=re.DOTALL,
)
if n != 1:
    raise SystemExit("Could not find exactly one SOLVED_COUNT marker block in README.md")

if new_text != text:
    README.write_text(new_text, encoding="utf-8")
    print(f"Updated solved count to {count}")
else:
    print(f"No change (still {count})")
