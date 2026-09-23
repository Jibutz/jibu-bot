import csv
from pathlib import Path

NECTA = Path(r"C:\Users\marti\OneDrive\Desktop\JIBU\necta-papers")
OUT = NECTA / "necta_questions_master.csv"

fieldnames = ["Subject", "Form_Level", "Topic", "Question", "Option_A", "Option_B", "Option_C", "Option_D", "Option_E", "Correct_Answer", "Explanation"]

source_files = [
    "biology_final.csv",
    "chemistry_final.csv",
    "english_final.csv",
    "geography_final.csv",
    "history_final.csv",
    "civics_final.csv",
]

all_rows = []
counts = {}
for fname in source_files:
    with open(NECTA / fname, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        assert reader.fieldnames == fieldnames, f"{fname} header mismatch: {reader.fieldnames}"
        rows = list(reader)
        subjects_seen = {r["Subject"] for r in rows}
        assert len(subjects_seen) == 1, f"{fname} has mixed Subject values: {subjects_seen}"
        all_rows.extend(rows)
        counts[fname] = (subjects_seen.pop(), len(rows))

with open(OUT, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(all_rows)

print(f"Wrote {len(all_rows)} rows to {OUT}")
for fname, (subject, n) in counts.items():
    print(f"  {subject}: {n} rows (from {fname})")
