import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from parse_mcq import get_text, parse_section_a  # noqa: E402

path = Path(sys.argv[1])
text = get_text(path)
items = parse_section_a(text)

# Cross-check: find raw "The correct answer is X" / "Correct answer: X" / "Answer: X"
# mentions in the whole document and make sure each parsed item's answer letter
# is self-consistent (options dict actually has that letter, and if the reason
# text itself asserts a specific letter via "correct answer is X", it matches).
problems = []
for it in items:
    letter = it["answer"]
    if letter not in it["options"]:
        problems.append(f"marker {it['marker']}: answer {letter} not in options {list(it['options'])}")
    # look for a stray "correct answer is <letter>" inside the reason that disagrees
    m = re.search(r"correct answer is\s*([A-E])\b", it["reason"], re.IGNORECASE)
    if m and m.group(1) != letter:
        problems.append(f"marker {it['marker']}: extracted answer {letter} but reason text says '{m.group(0)}'")

print(f"{path.name}: {len(items)} items, {len(problems)} problems")
for p in problems:
    print("  !!", p)
