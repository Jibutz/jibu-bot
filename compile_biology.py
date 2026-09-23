import csv
import json
from pathlib import Path

RAW = Path(r"C:\Users\marti\OneDrive\Desktop\JIBU\raw_text")
OUT = Path(r"C:\Users\marti\OneDrive\Desktop\JIBU\necta-papers\biology_final.csv")

def load(name):
    return json.loads((RAW / name).read_text(encoding="utf-8-sig"))

topics_1996 = ["Cell Specialization", "Fish Respiration", "Plant Classification", "Photosynthesis",
               "Respiration and Energy", "Circulatory System", "Soil Properties", "Human Eye",
               "Genetics and Inheritance", "Ecological Succession"]
topics_2021 = ["Amphibian Respiration", "Laboratory Apparatus", "First Aid", "Cell Biology",
               "Digestion", "Human Eye", "Seed Germination", "Parasitic Worms",
               "Ecosystems and Food Chains", "Plant Transport"]
topics_2022 = ["Nervous System", "Waste Management", "Excretory System", "Genetics and Inheritance",
               "Seed Structure", "Natural Selection", "Plant Transport", "Animal Classification",
               "Muscles and Movement", "Cell Structure"]
topics_2025 = ["Scientific Method", "Food Chains", "Fermentation", "Reproductive Health",
               "Thermoregulation", "Global Diseases", "Safety Precautions", "Skeletal System",
               "Genetics and Inheritance", "Animal Classification"]
topics_2024 = ["Excretory System", "Laboratory Apparatus", "Kidney Disorders", "Thermoregulation",
               "Cell Structure", "Darwin's Theory", "Plant Reproduction", "Endocrine System",
               "Classification", "DNA Structure"]

rows = []

for fname, topics in [
    ("bio_Biology1-F4-1996-Solutions.pdf.json", topics_1996),
    ("bio_Biology1-F4-2021-Solutions.pdf.json", topics_2021),
    ("bio_Biology1-F4-2022-Solutions.pdf.json", topics_2022),
    ("bio_Biology1-F4-2025-Solutions.pdf.json", topics_2025),
]:
    items = load(fname)
    assert len(items) == 10, f"{fname}: expected 10, got {len(items)}"
    for item, topic in zip(items, topics):
        opts = item["options"]
        rows.append(dict(
            Subject="Biology", Form_Level="Form 4", Topic=topic,
            Question=item["question"],
            Option_A=opts.get("A", ""), Option_B=opts.get("B", ""), Option_C=opts.get("C", ""),
            Option_D=opts.get("D", ""), Option_E=opts.get("E", ""),
            Correct_Answer=item["answer"], Explanation=item["reason"],
        ))

# 2024: 9 auto-parsed items, with item v's polluted reason fixed, plus the manually
# re-derived Darwin item (vi) inserted in its correct position between v and vii.
items_2024 = load("bio_Biology1-F4-2024-Solutions.pdf.json")
assert len(items_2024) == 9, f"2024: expected 9 auto items, got {len(items_2024)}"
items_2024[4]["reason"] = ("The nucleus contains genetic material and directs all cellular processes "
                            "such as growth, metabolism, and reproduction.")

darwin_item = {
    "question": ("Which statements support the Darwin's theory of organic evolution? "
                 "(i) Living organisms produce more offspring than the environment can support. "
                 "(ii) An individual is able to develop structures to suit the need of the environment. "
                 "(iii) Organisms struggle for existence over limited resources such as mates. "
                 "(iv) The fittest organisms survive while the less adapted are eliminated. "
                 "(v) The more an individual used a part of its body the more developed that part became."),
    "options": {
        "A": "(i), (ii) and (iii)", "B": "(i), (ii) and (iv)", "C": "(i), (iii) and (iv)",
        "D": "(ii), (iv) and (v)", "E": "(iii), (iv) and (v)",
    },
    "answer": "C",
    "reason": ("Overproduction of offspring, struggle for existence, and survival of the fittest are the "
               "core points of Darwin's theory of natural selection; (ii) and (v) instead describe "
               "Lamarck's theory of acquired characteristics."),
}

items_2024_full = items_2024[:5] + [darwin_item] + items_2024[5:]
assert len(items_2024_full) == 10

for item, topic in zip(items_2024_full, topics_2024):
    opts = item["options"]
    rows.append(dict(
        Subject="Biology", Form_Level="Form 4", Topic=topic,
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
