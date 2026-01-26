#!/usr/bin/env python3
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"

# === CONFIG ===
FONT = "bigmono12"   # toilet font (change if you want)
WIDTH = 60            # display width for centering
# ==============

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

# --- count solution links (GitHub URLs in this repo) ---
targets = re.findall(r"\[[^\]]+\]\(([^)]+)\)", region)

solution_url = re.compile(
    r"^https://github\.com/gevorg-hunanyan/taocp-solutions/blob/main/.*/ex\d+\.\w+$",
    re.IGNORECASE,
)

count = sum(1 for t in targets if solution_url.match(t.strip()))

# --- 1) update normal text counter ---
text2, n1 = re.subn(
    r"(<!--\s*SOLVED_COUNT\s*-->)(.*?)(<!--\s*/SOLVED_COUNT\s*-->)",
    lambda m: f"{m.group(1)}{count}{m.group(3)}",
    text,
    flags=re.DOTALL,
)
if n1 != 1:
    raise SystemExit("Could not find exactly one SOLVED_COUNT marker block")

# --- 2) generate ASCII (NUMBER ONLY) ---
ascii_raw = subprocess.check_output(
    ["toilet", "-f", FONT, str(count)],
    text=True,
)

lines = ascii_raw.splitlines()

# remove ALL leading blank lines
while lines and not lines[0].strip():
    lines.pop(0)

# remove ALL trailing blank lines
while lines and not lines[-1].strip():
    lines.pop()

def center_line(line: str) -> str:
    pad = max((WIDTH - len(line)) // 2, 0)
    return " " * pad + line

ascii_centered = "\n".join(center_line(line) for line in lines)
ascii_block = f"```\n{ascii_centered}\n```"

# --- 3) update ASCII block ---
text3, n2 = re.subn(
    r"(<!--\s*SOLVED_ASCII_START\s*-->)(.*?)(<!--\s*SOLVED_ASCII_END\s*-->)",
    lambda m: f"{m.group(1)}\n{ascii_block}\n{m.group(3)}",
    text2,
    flags=re.DOTALL,
)
if n2 != 1:
    raise SystemExit("SOLVED_ASCII markers not found exactly once")

# --- write if changed ---
if text3 != text:
    README.write_text(text3, encoding="utf-8")
    print(f"Updated solved count to {count} (text + ASCII)")
else:
    print("No change")
