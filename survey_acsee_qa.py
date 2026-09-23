import re
import sys
from pathlib import Path

import pdfplumber

def get_text(path):
    with pdfplumber.open(path) as pdf:
        return "\n".join((p.extract_text() or "") for p in pdf.pages)


def main():
    folder = Path(sys.argv[1])
    pattern = sys.argv[2]
    rx = re.compile(pattern)
    files = []
    for f in sorted(folder.glob("*-Solutions.pdf")):
        m = rx.match(f.name)
        if m:
            files.append((int(m.group(1)), f))
    files.sort()

    for year, f in files:
        text = get_text(f)
        # crude proxy for "has real worked answers": total text length after
        # the instructions block, and how many numbered top-level questions
        # ("N. (a)" or "N." at line start) appear
        body_start = re.search(r"Prepared by:?\s*Maria Marco for TETEA", text)
        body = text[body_start.end():] if body_start else text
        body = re.sub(r"Find this and other free resources.*|Prepared by:?\s*Maria Marco for TETEA|--- PAGE \d+ ---", "", body)
        q_markers = len(re.findall(r"\n\s*\d{1,2}\.\s*\(?[a-zA-Z]?\)?", body))
        char_count = len(body.strip())
        avg_per_q = char_count / q_markers if q_markers else 0
        flag = "OK" if avg_per_q >= 200 else "SUSPECT (short/bare)"
        print(f"{year}: chars={char_count} q_markers={q_markers} avg/marker={avg_per_q:.0f} [{flag}]")


if __name__ == "__main__":
    main()
