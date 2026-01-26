#!/usr/bin/env python3
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"

text = README.read_text(encoding="utf-8")

# Extract only the “solutions” region
m = re.search(
    r"<!--\s*SOLUTIONS_START\s*-->(.*?)(<!--\s*SOLUTIONS_END\s*-->|$)",
    text,
    flags=re.DOTALL
)
if not m:
    raise SystemExit("Couldn't find <!-- SOLUTIONS_START --> marker in README.md")

region = m.group(1)

# Count Markdown links: [title](target)
links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", region)

def is_solution_link(target: str) -> bool:
    t = target.strip()
    # Ignore external links, mailto, anchors
    if t.startswith(("http://", "https://", "mailto:", "#")):
        return False
    return True

count = sum(1 for t in links if is_solution_link(t))

# Update the counter placeholder anywhere in README
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
