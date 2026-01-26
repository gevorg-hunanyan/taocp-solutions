#!/usr/bin/env python3
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"

text = README.read_text(encoding="utf-8")

# --- extract solutions region ---
m = re.search(
    r"<!--\s*SOLUTIONS_START\s*-->(.*?)(<!--\s*SOLUTIONS_END\s*-->|$)",
    text,
    flags=re.DOTALL,
)
if not m:
    raise SystemExit("Missing SOLUTIONS_START marker")

region = m.group(1)

# --- count solution links ---
targets = re.findall(r"\[[^\]]+\]\(([^)]+)\)", region)

solution_url = re.compile(
    r"^https://github\.com/gevorg-hunanyan/taocp-solutions/blob/main/.*/ex\d+\.\w+$",
    re.IGNORECASE,
)

count = sum(1 for t in targets if solution_url.match(t.strip()))

# --- generate ASCII with figlet ---
try:
    ascii_number = subprocess.check_output(
        ["figlet", "-f", "big", str(count)],
        text=True
    )
except FileNotFoundError:
    raise SystemExit("figlet is not installed")

ascii_block = f"```\n{ascii_number.rstrip()}\n```"

# --- replace README block ---
new_text, n = re.subn(
    r"(<!--\s*SOLVED_ASCII_START\s*-->)(.*?)(<!--\s*SOLVED_ASCII_END\s*-->)",
    lambda m: f"{m.group(1)}\n{ascii_block}\n{m.group(3)}",
    text,
    flags=re.DOTALL,
)

if n != 1:
    raise SystemExit("SOLVED_ASCII markers not found exactly once")

if new_text != text:
    README.write_text(new_text, encoding="utf-8")
    print(f"Updated ASCII solved count to {count}")
else:
    print("No change")
