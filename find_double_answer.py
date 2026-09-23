import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from parse_mcq import get_text, ANCHOR_RE, MARKER_RE, get_section_a_bounds  # noqa: E402

path = Path(sys.argv[1])
text = get_text(path)

bounds = get_section_a_bounds(text)
if bounds is None:
    print(f"{path.name}: could not locate Section A")
    sys.exit(0)
section_start, section_end = bounds
section = text[section_start:section_end]

markers = list(MARKER_RE.finditer(section))
anchors = list(ANCHOR_RE.finditer(section))

# crude: for each pair of consecutive markers, count how many "Answer:"/"Correct
# answer:" anchors fall strictly between them - should be exactly 1
positions = [m.start() for m in markers] + [len(section)]
for i in range(len(positions) - 1):
    lo, hi = positions[i], positions[i + 1]
    count = sum(1 for a in anchors if lo < a.start() < hi)
    if count > 1:
        print(f"{path.name}: {count} answer-anchors after marker #{i+1} (possible duplicate/self-correction)")
