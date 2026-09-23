import csv
import json
from pathlib import Path

RAW = Path(r"C:\Users\marti\OneDrive\Desktop\JIBU\raw_text")
OUT = Path(r"C:\Users\marti\OneDrive\Desktop\JIBU\necta-papers\history_final.csv")

def load(name):
    return json.loads((RAW / name).read_text(encoding="utf-8-sig"))

topics_2021 = ["Basic Human Needs", "African Political Systems", "Historical Sources", "Historical Sources",
               "Industrial Revolution", "Human Evolution", "African Migrations", "Slave Trade",
               "Colonial Economy", "Colonial Administration", "East African Coast History",
               "League of Nations", "Anti-Colonial Resistance", "Human Evolution", "United Nations"]
topics_2022 = ["Historical Sources", "Colonial Administration", "French Revolution", "Human Evolution",
               "American Independence", "Anti-Colonial Resistance", "Tanzania Military",
               "Nationalist Movements", "European Exploration", "Colonial Administration",
               "Nationalist Movements", "Julius Nyerere", "League of Nations", "Zimbabwe Independence",
               "European Exploration"]
topics_2024 = ["Time Concepts", "Human Evolution", "Trans-Saharan Trade", "African Kingdoms",
               "Colonial Administration", "Pre-Colonial Economy", "Modes of Production",
               "Early Trade Contacts", "Scramble for Africa", "Neo-Colonialism"]
topics_2025 = ["Historical Sources", "Human Evolution", "Anti-Colonial Resistance", "Colonial Education",
               "Colonial Economy", "Modes of Production", "Zanzibar Revolution", "Value of History",
               "Colonial Administration", "African Kingdoms"]

rows = []

def add_rows(items, topics):
    for item, topic in zip(items, topics):
        opts = item["options"]
        rows.append(dict(
            Subject="History", Form_Level="Form 4", Topic=topic,
            Question=item["question"],
            Option_A=opts.get("A", ""), Option_B=opts.get("B", ""), Option_C=opts.get("C", ""),
            Option_D=opts.get("D", ""), Option_E=opts.get("E", ""),
            Correct_Answer=item["answer"], Explanation=item["reason"],
        ))

# 2021: all 15 items parsed cleanly, verified against raw text.
items_2021 = load("hist_2021.json")
assert len(items_2021) == 15, f"2021: expected 15, got {len(items_2021)}"
add_rows(items_2021, topics_2021)

# 2022: 14 auto-parsed + item vii manually re-derived (swallowed into item vi's
# reason by the nested (i)-(iv) sub-statement list, same class of issue as the
# Biology Darwin question).
items_2022 = load("hist_2022.json")
assert len(items_2022) == 14, f"2022 auto: expected 14 (item vii missing), got {len(items_2022)}"
items_2022[5]["reason"] = ("Samora Machel (Mozambique) and Agostinho Neto (Angola) led struggles against "
                            "Portuguese colonial rule.")
military_item = {
    "question": ("What were the objectives of establishing national military institutions in Tanzania? "
                 "(i) To protect the country from external aggression (ii) To promote internal security and "
                 "integrity (iii) To participate in national building activities (iv) To urge states to "
                 "conform to peaceful settlement of disputes"),
    "options": {
        "A": "(i), (ii) and (iv)", "B": "(i), (iii) and (ii)", "C": "(i), (iii) and (iv)",
        "D": "(i) and (iv) only", "E": "(iii), (ii) and (iv)",
    },
    "answer": "B",
    "reason": ("National military institutions in Tanzania were established primarily to protect against "
               "external threats, contribute to internal stability, and participate in nation-building efforts."),
}
items_2022_full = items_2022[:6] + [military_item] + items_2022[6:]
assert len(items_2022_full) == 15
add_rows(items_2022_full, topics_2022)

# 2023 is excluded entirely: every item in the source PDF has a bare
# "Correct Answer: X" with NO "Reason:"/explanation text at all (verified
# against the raw PDF text) - it fails the "must have full Answer + Reason
# explanations" rule, it just wasn't caught by the automated BARE/DETAILED
# classifier because one item's reason field accidentally absorbed the next
# item's question stem (a parsing artifact, not a real explanation).

# 2024, 2025: both parsed cleanly, 10 items each, verified.
items_2024 = load("hist_2024.json")
assert len(items_2024) == 10
add_rows(items_2024, topics_2024)

items_2025 = load("hist_2025.json")
assert len(items_2025) == 10
add_rows(items_2025, topics_2025)

fieldnames = ["Subject", "Form_Level", "Topic", "Question", "Option_A", "Option_B", "Option_C", "Option_D", "Option_E", "Correct_Answer", "Explanation"]
with open(OUT, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Wrote {len(rows)} rows to {OUT}")
