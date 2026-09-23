import csv
import json
from pathlib import Path

RAW = Path(r"C:\Users\marti\OneDrive\Desktop\JIBU\raw_text")
OUT = Path(r"C:\Users\marti\OneDrive\Desktop\JIBU\necta-papers\chemistry_final.csv")

def load(name):
    return json.loads((RAW / name).read_text(encoding="utf-8-sig"))

topics = {
    "2001": ["Separation Techniques", "Atomic Structure", "Acids and Bases", "Scientific Skills",
             "Periodic Table", "Energy Changes", "Empirical Formula", "Allotropy",
             "Chemical Equations", "Electrolysis"],
    "2006": ["Fertilizers", "Chemical Changes", "Esterification", "Energy Changes",
             "Acids and Bases", "Mole Calculations", "Ionic Equations", "Organic Chemistry",
             "Redox Reactions", "Periodic Table"],
    "2018": ["Applied Chemistry", "Electrolysis", "Redox Reactions", "Thermal Stability",
             "Metal Reactivity", "Organic Chemistry", "Chemical Equilibrium", "Combustion",
             "Combustion", "Extraction of Metals"],
    "2021": ["Fire Safety", "Fire Safety", "Chemical Changes", "Empirical Formula",
             "Chemical Nomenclature", "Types of Reactions", "Particulate Nature of Matter",
             "Soil Chemistry", "Atomic Structure", "Extraction of Metals"],
    "2022": ["Properties of Water", "Atomic Structure", "Fuels and Energy", "Particulate Nature of Matter",
             "Fuels and Energy", "Organic Chemistry", "Safety and First Aid", "Redox Reactions",
             "Fire Safety", "Separation Techniques"],
    "2024": ["Atomic Theory", "Organic Chemistry", "Periodic Table", "Periodic Table",
             "Scientific Method", "Properties of Water", "Oxides", "Electrolysis",
             "Corrosion", "Types of Reactions"],
    "2025": ["States of Matter", "Redox Reactions", "Chemical Tests", "Fire Safety",
             "Fuels and Energy", "Gas Preparation", "Mole Calculations", "Fuels and Energy",
             "Gas Preparation"],  # only 9 - item ii dropped (irreparable subscript corruption)
}

rows = []
for year in ["2001", "2006", "2018", "2021", "2022", "2024"]:
    items = load(f"chem_{year}.json")
    assert len(items) == 10, f"{year}: expected 10, got {len(items)}"
    for item, topic in zip(items, topics[year]):
        opts = item["options"]
        rows.append(dict(
            Subject="Chemistry", Form_Level="Form 4", Topic=topic,
            Question=item["question"],
            Option_A=opts.get("A", ""), Option_B=opts.get("B", ""), Option_C=opts.get("C", ""),
            Option_D=opts.get("D", ""), Option_E=opts.get("E", ""),
            Correct_Answer=item["answer"], Explanation=item["reason"],
        ))

# 2025: drop item ii (molecular formula question) - its subscripted chemical
# formulas were mangled beyond faithful reconstruction by the PDF text
# extractor (e.g. "C H\n2 6" instead of C2H6), and guessing at the real
# formulas would violate "pull from the actual source, don't guess".
items_2025 = load("chem_2025.json")
assert len(items_2025) == 10
items_2025_kept = [it for idx, it in enumerate(items_2025) if idx != 1]
assert len(items_2025_kept) == 9
for item, topic in zip(items_2025_kept, topics["2025"]):
    opts = item["options"]
    rows.append(dict(
        Subject="Chemistry", Form_Level="Form 4", Topic=topic,
        Question=item["question"],
        Option_A=opts.get("A", ""), Option_B=opts.get("B", ""), Option_C=opts.get("C", ""),
        Option_D=opts.get("D", ""), Option_E=opts.get("E", ""),
        Correct_Answer=item["answer"], Explanation=item["reason"],
    ))

fieldnames = ["Subject", "Form_Level", "Topic", "Question", "Option_A", "Option_B", "Option_C", "Option_D", "Option_E", "Correct_Answer", "Explanation"]
with open(OUT, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Wrote {len(rows)} rows to {OUT}")
