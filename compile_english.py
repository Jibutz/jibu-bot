import csv
import json
from pathlib import Path

RAW = Path(r"C:\Users\marti\OneDrive\Desktop\JIBU\raw_text")
OUT = Path(r"C:\Users\marti\OneDrive\Desktop\JIBU\necta-papers\english_final.csv")

def load(name):
    return json.loads((RAW / name).read_text(encoding="utf-8-sig"))

rows = []

def add_rows(items, topics):
    assert len(items) == len(topics), f"{len(items)} items vs {len(topics)} topics"
    for item, topic in zip(items, topics):
        opts = item["options"]
        rows.append(dict(
            Subject="English", Form_Level="Form 4", Topic=topic,
            Question=item["question"],
            Option_A=opts.get("A", ""), Option_B=opts.get("B", ""), Option_C=opts.get("C", ""),
            Option_D=opts.get("D", ""), Option_E=opts.get("E", ""),
            Correct_Answer=item["answer"], Explanation=item["reason"],
        ))

# ----- Comprehension-passage years: every item shares one topic -----
for fname, count in [("eng_2001.json", 10), ("eng_2004.json", 9), ("eng_2005.json", 10), ("eng_2006.json", 10)]:
    items = load(fname)
    assert len(items) == count, f"{fname}: expected {count}, got {len(items)}"
    add_rows(items, ["Reading Comprehension"] * count)

# ----- 2003: fully manually re-derived. This paper has a different overall
# structure than every other year - MCQs are scattered across three separate
# top-level questions (Q1 comprehension, Q7 grammar fill-ins, Q9 vocabulary),
# each restarting its own (i)-(...) numbering, rather than one Section A
# block of 10. The automated parser's "18 items" count was actually correct
# (10+4+4=18) but with garbled item boundaries at the Q1->Q7->Q9 seams, so
# every item below was read directly from the raw PDF text. -----
items_2003 = [
    {"question": "\u201cAn idle mind is the devil\u2019s workshop\u201d means", "options": {
        "A": "satan is cleverer than our hands", "B": "satan is an employer to people",
        "C": "people who are jobless are welcome for work",
        "D": "people with nothing to do can be directed to do evil things by satan",
        "E": "satan finds work to obedient hands to do"}, "answer": "D",
     "reason": "The proverb means that when people are idle, they are more likely to engage in wrong or harmful actions."},
    {"question": "Paragraph one suggests that", "options": {
        "A": "self employment and good use of time makes one active",
        "B": "much activity leads to boredom and unlawful spending of time",
        "C": "everyone should avoid falling into bad things",
        "D": "unlawful ways of spending free time encourage pleasure",
        "E": "there is no work without satan\u2019s temptations"}, "answer": "A",
     "reason": "The first paragraph stresses that using free time wisely prevents boredom and bad habits."},
    {"question": "A hobby can be", "options": {
        "A": "anything that is done physically by an individual",
        "B": "either physical or mental activity that entertains at extra time",
        "C": "anything that is done inside normal routine at school or workplace to entertain",
        "D": "games or athletics within the school routine",
        "E": "anything that is done in the same way as different much work"}, "answer": "B",
     "reason": "The passage defines a hobby as a physical, mental, or entertainment activity done outside normal routine."},
    {"question": "Stamp collection results into", "options": {
        "A": "an expensive hobby which is useless", "B": "correspondence in pictures and designs",
        "C": "acquisition of educational knowledge",
        "D": "cheap collection from stamp dealers who are overseas",
        "E": "boredom of geographical and historical information"}, "answer": "C",
     "reason": "The passage states stamp collecting provides geographical and historical knowledge."},
    {"question": "An album as used in the passage means", "options": {
        "A": "an interesting short playing record", "B": "a book written about stamp collection",
        "C": "an order of countries collecting stamps", "D": "a book with little writing for collecting stamps",
        "E": "a book with pictures drawn in it"}, "answer": "D",
     "reason": "Stamp collectors use an album as a book to keep and arrange their stamps."},
    {"question": "A stamp collector has an advantage in that", "options": {
        "A": "he can reuse the stamps collected in the album", "B": "he keeps stamps of flowers or animals only",
        "C": "the more he keeps them the more valuable they become",
        "D": "he arranges stamps from one country only", "E": "stamp dealers know each other"}, "answer": "C",
     "reason": "The passage explains that stamps gain value the longer they are preserved."},
    {"question": "\u201cDepicting\u201d as used in the third paragraph means", "options": {
        "A": "showing", "B": "represent", "C": "explain", "D": "drawing", "E": "collecting"}, "answer": "A",
     "reason": "\u201cDepicting\u201d means showing or illustrating something."},
    {"question": "The introduction of machines and other gadgets has changed people to", "options": {
        "A": "have more time to rest than working", "B": "become important in the society",
        "C": "learn more modern things", "D": "use spare time more constructively",
        "E": "earn more money than before"}, "answer": "A",
     "reason": "Machines reduce workload, giving people more leisure time."},
    {"question": "The last paragraph suggests that", "options": {
        "A": "it is important in the future to use spare time", "B": "one can earn more money than before",
        "C": "machines and labour gadgets are important", "D": "future is an important element of time",
        "E": "an alternative to leisure time is the hobby"}, "answer": "A",
     "reason": "The final paragraph emphasizes that with more free time, people must learn to use it wisely."},
    {"question": "The best title for the passage is", "options": {
        "A": "the leisure time", "B": "an old saying", "C": "the importance of a hobby",
        "D": "satan finds work", "E": "stamp collecting"}, "answer": "C",
     "reason": "The passage focuses on explaining what a hobby is, its values, and why it is important."},
    {"question": "Juma and Mary used to be good friends, but now they have -----", "options": {
        "A": "fallen off", "B": "turned off", "C": "given in", "D": "fallen out", "E": "put out"}, "answer": "D",
     "reason": "\u201cFallen out\u201d means to quarrel or stop being friends."},
    {"question": "When the light went off, I ----- my supper.", "options": {
        "A": "have eaten", "B": "have been eating", "C": "was eating", "D": "had ate", "E": "am eating"}, "answer": "C",
     "reason": "Past continuous tense shows an action that was happening when another occurred."},
    {"question": "There was not ----- traffic on that road last night.", "options": {
        "A": "much", "B": "many", "C": "lot of", "D": "a few", "E": "a little"}, "answer": "A",
     "reason": "\u201cTraffic\u201d is uncountable, so \u201cmuch traffic\u201d is correct."},
    {"question": "If the boat had been maintained properly, it ----- capsized.", "options": {
        "A": "will not have", "B": "would not have", "C": "will not", "D": "would not", "E": "might not"}, "answer": "B",
     "reason": "This is a third conditional sentence about a past unreal situation."},
    {"question": "They asked the secretary to summon a meeting of the Sports Council.", "options": {
        "A": "Lead", "B": "Control", "C": "Call", "D": "Postpone", "E": "All end"}, "answer": "C",
     "reason": "\u201cSummon\u201d means to call for or request attendance."},
    {"question": "The attitude of the gate keeper was very hostile.", "options": {
        "A": "Strange", "B": "Unfriendly", "C": "Patient", "D": "Abusive", "E": "Welcoming"}, "answer": "B",
     "reason": "\u201cHostile\u201d means unfriendly or aggressive."},
    {"question": "It seems that we will have to differ on the amount of money to be spent for the graduation ceremony.", "options": {
        "A": "Disagree", "B": "Quarrel", "C": "Speak", "D": "Think", "E": "Forget"}, "answer": "A",
     "reason": "\u201cDiffer on\u201d means to disagree."},
    {"question": "A more durable paint was used for outside walls.", "options": {
        "A": "Attractive", "B": "Decorative", "C": "Expensive", "D": "Shiny", "E": "Lasting"}, "answer": "E",
     "reason": "\u201cDurable\u201d means long-lasting."},
]
topics_2003 = (["Reading Comprehension"] * 10
               + ["Idiomatic Expressions", "Verb Tenses", "Countable and Uncountable Nouns", "Conditional Sentences"]
               + ["Vocabulary in Context"] * 4)
add_rows(items_2003, topics_2003)

# ----- Grammar/vocabulary-focused years -----
topics = {
    "eng_2019.json": ["Verb Tenses", "Verb Tenses", "Subject-Verb Agreement", "Verb Tenses",
                       "Subject-Verb Agreement", "Verb Tenses", "Verb Tenses", "Verb Tenses",
                       "Verb Tenses", "Articles"],
    "eng_2020.json": ["Verb Tenses", "Verb Forms", "Verb Tenses", "Verb Tenses", "Subject-Verb Agreement",
                       "Verb Tenses", "Verb Tenses", "Verb Tenses", "Verb Tenses", "Articles"],
    "eng_2021.json": ["Conditional Sentences", "Question Tags", "Sentence Structure", "Vocabulary in Context",
                       "Formal Language", "Letter Writing", "Writing Skills", "Fact and Opinion",
                       "Formal Writing", "Public Speaking"],
    "eng_2022.json": ["Descriptive Language", "Vocabulary in Context", "Grammar Usage", "Vocabulary in Context",
                       "Articles", "Verb Tenses", "Verb Tenses", "Verb Tenses", "Reported Speech",
                       "Question Formation"],
    "eng_2023.json": ["Vocabulary in Context", "Vocabulary in Context", "Vocabulary in Context",
                       "Vocabulary in Context", "Formal Writing", "Reported Speech", "Fact and Opinion",
                       "Formal Language", "Sentence Structure", "Writing Skills"],
    "eng_2024.json": ["Vocabulary in Context", "Grammar Usage", "Formal Writing", "Reference Skills",
                       "Verb Tenses", "Reading Comprehension", "Verb Tenses", "Fact and Opinion",
                       "Grammar Usage", "Vocabulary in Context"],
    "eng_2025.json": ["Vocabulary in Context", "Grammar Usage", "Verb Tenses", "Vocabulary in Context",
                       "Reference Skills", "Grammar Usage", "Verb Tenses", "Verb Tenses",
                       "Vocabulary in Context", "Letter Writing"],
}
for fname, topic_list in topics.items():
    items = load(fname)
    assert len(items) == 10, f"{fname}: expected 10, got {len(items)}"
    add_rows(items, topic_list)

# clean up the garbled table text in eng_2024 item vi (index 5)
for row in rows:
    if row["Question"].startswith("Study the following table and answer"):
        row["Question"] = ("Study the following table showing what Jane likes and dislikes, where X means "
                            "dislikes: Pets \u2013 likes; Chickens \u2013 X; Giraffes \u2013 X; Zebra \u2013 likes. "
                            "Which of the following expressions describes best what Jane likes?")

fieldnames = ["Subject", "Form_Level", "Topic", "Question", "Option_A", "Option_B", "Option_C", "Option_D", "Option_E", "Correct_Answer", "Explanation"]
with open(OUT, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Wrote {len(rows)} rows to {OUT}")
