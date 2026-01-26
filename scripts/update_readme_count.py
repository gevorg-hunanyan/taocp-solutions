#!/usr/bin/env python3
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"

FONT = "mono12"  # toilet font
WIDTH = 80       # for fake-centering

text = README.read_text(encoding="utf-8")

# --- extract solutions region ---
m = re.search(
    r"<!--\s*SOLUTIONS_START\s*-->(.*?)(<!--\s*SOLUTIONS_END\s*-->|$)",
    text,
    flags=re.DOTALL,
)
if not m:
    raise SystemExit("Missing SOLUTIONS_START marker in README.md")

region = m.group(1)

# --- count links in your repo (GitHub URLs) ---
targets = re.findall(r"\[[^\]]+\]\(([^)]+)\)", region)

solution_url = re.compile(
    r"^https://github\.com/gevorg-hunanyan/taocp-solutions/blob/main/.*/ex\d+\.\w+$",
    re.IGNORECASE,
)
count = sum(1 for t in targets if solution_url.match(t.strip()))

# --- 1) Update normal text marker: <!-- SOLVED_COUNT -->N<!-- /SOLVED_COUNT -->
text2, n1 = re.subn(
    r"(<!--\s*SOLVED_COUNT\s*-->)(.*?)(<!--\s*/SOLVED_COUNT\s*-->)",
    lambda mm: f"{mm.group(1)}{count}{mm.group(3)}",
    text,
    flags=re.DOTALL,
)
if n1 != 1:
    raise SystemExit("Could not find exactly one SOLVED_COUNT marker block in README.md")

# --- 2) Generate ASCII for "Solved: N" using toilet ---
label = str(count)
ascii_raw = subprocess.check_output(["toilet", "-f", FONT, label], text=True)

lines = ascii_raw.rstrip().splitlines()
def center_line(line: str) -> str:
    pad = max((WIDTH - len(line)) // 2, 0)
    return " " * pad + line

ascii_centered = "\n".join(center_line(line) for line in lines)
ascii_block = f"```\n{ascii_centered}\n```"

# --- 3) Update ASCII marker block ---
text3, n2 = re.subn(
    r"(<!--\s*SOLVED_ASCII_START\s*-->)(.*?)(<!--\s*SOLVED_ASCII_END\s*-->)",
    lambda mm: f"{mm.group(1)}\n{ascii_block}\n{mm.group(3)}",
    text2,
    flags=re.DOTALL,
)
if n2 != 1:
    raise SystemExit("SOLVED_ASCII markers not found exactly once in README.md")

# --- write if changed ---
if text3 != text:
    README.write_text(text3, encoding="utf-8")
    print(f"Updated solved count to {count} (text + ASCII)")
else:
    print("No change")
