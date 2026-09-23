import re
import sys
from pathlib import Path

import pdfplumber

def classify(path):
    try:
        with pdfplumber.open(path) as pdf:
            text = ""
            for page in pdf.pages:
                text += (page.extract_text() or "") + "\n"
    except Exception as e:
        return "ERROR", str(e), 0

    reason_count = len(re.findall(r"\bReason\s*:", text, re.IGNORECASE))
    answer_count = len(re.findall(r"\bAnswer\s*:", text, re.IGNORECASE))
    return ("DETAILED" if reason_count >= 5 else "BARE"), reason_count, answer_count


if __name__ == "__main__":
    folder = Path(sys.argv[1])
    pattern = sys.argv[2]  # e.g. "Biology1-F4-*-Solutions.pdf"
    files = sorted(folder.glob(pattern))
    for f in files:
        label, reason_count, answer_count = classify(f)
        print(f"{label}\treason={reason_count}\tanswer={answer_count}\t{f.name}")
