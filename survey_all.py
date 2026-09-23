import re
import sys
from pathlib import Path

import pdfplumber

sys.path.insert(0, str(Path(__file__).parent))
from parse_mcq import parse_section_a  # noqa: E402

BASE = Path(r"C:\Users\marti\OneDrive\Desktop\JIBU\necta-papers")

SUBJECTS = {
    "biology": ("biology", r"^Biology1-F4-(\d{4})-Solutions\.pdf$"),
    "chemistry": ("chemistry", r"^Chemistry1-F4-(\d{4})-Solutions\.pdf$"),
    "english": ("english", r"^English-F4-(\d{4})-Solutions\.pdf$"),
    "geography": ("geography", r"^Geography-F4-(\d{4})-Solutions\.pdf$"),
    "history": ("history", r"^History-F4-(\d{4})-Solutions\.pdf$"),
    "civics": ("civics", r"^Civics-F4-(\d{4})-Solutions\.pdf$"),
    "basic-maths": ("basic-maths", r"^BasicMath-F4-(\d{4})-Solutions\.pdf$"),
}


def get_text(path):
    with pdfplumber.open(path) as pdf:
        return "\n".join((p.extract_text() or "") for p in pdf.pages)


def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    grand_total = 0
    for subj, (folder, pattern) in SUBJECTS.items():
        if only and subj != only:
            continue
        folder_path = BASE / folder
        rx = re.compile(pattern)
        files = []
        for f in sorted(folder_path.glob("*-Solutions.pdf")):
            m = rx.match(f.name)
            if m:
                files.append((int(m.group(1)), f))
        files.sort()

        print(f"\n=== {subj} ({len(files)} year-files found) ===")
        subj_total = 0
        detailed_years = []
        for year, f in files:
            text = get_text(f)
            items = parse_section_a(text)
            avg_reason_len = (
                sum(len(it["reason"]) for it in items) / len(items) if items else 0
            )
            is_detailed = len(items) >= 8 and avg_reason_len >= 15
            if not is_detailed:
                print(f"  {year}: BARE/UNSUPPORTED (parsed={len(items)}, avg_reason_len={avg_reason_len:.0f}) -- skipped")
                continue
            status = "OK" if len(items) == 10 else "PARSE-ISSUE (needs manual patch)"
            print(f"  {year}: DETAILED -> parsed {len(items)} items [{status}]")
            subj_total += len(items)
            detailed_years.append(year)
        print(f"  -> {subj}: {len(detailed_years)} detailed years, {subj_total} questions")
        grand_total += subj_total
    print(f"\nGRAND TOTAL so far: {grand_total}")


if __name__ == "__main__":
    main()
