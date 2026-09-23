import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from parse_mcq import get_text, parse_section_a  # noqa: E402

path = Path(sys.argv[1])
text = get_text(path)
items = parse_section_a(text)
print(json.dumps(items, indent=1, ensure_ascii=False))
