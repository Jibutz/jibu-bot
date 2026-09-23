import re
import sys
from pathlib import Path

import pdfplumber

MARKER_RE = re.compile(r"\(([ivx]+)\)\s*")
OPTION_LINE_RE = re.compile(r"^([A-E])[ .]\s*(.*)$")
ANCHOR_RE = re.compile(r"(?:Correct answer|Answer)\s*:\s*", re.IGNORECASE)


def get_text(path):
    with pdfplumber.open(path) as pdf:
        return "\n".join((p.extract_text() or "") for p in pdf.pages)


def clean(s):
    s = re.sub(r"\s+", " ", s).strip()
    s = re.sub(r"\d*\s*Find this and other free resources at:?\s*\S*", "", s, flags=re.IGNORECASE)
    s = re.sub(r"Prepared by:?\s*Maria Marco for TETEA", "", s, flags=re.IGNORECASE)
    s = re.sub(r"\bPage \d+ of\s*\d*\b", "", s, flags=re.IGNORECASE)
    s = re.sub(r"^Explanation:\s*", "", s, flags=re.IGNORECASE)
    return re.sub(r"\s+", " ", s).strip()


PAGE_NOISE_RE = re.compile(
    r"^(\d+|Find this and other free resources.*|Prepared by:?\s*Maria Marco for TETEA|Page \d+ of\s*\d*)$",
    re.IGNORECASE,
)


def parse_options(stem_options_text):
    # A stem line that happens to start with a capital letter A-E (e.g. "A Form
    # Four student boiled..." or "A delta which is found...") can be mistaken
    # for an option line by naive forward scanning. Options are always the
    # LAST few lines of this block (right before "Answer:"), so scan backward
    # from the end, requiring a strict E,D,C,B,A (or D,C,B,A) descending run.
    # This anchors on the known-safe end and stops the instant a full run
    # down to "A" is found, so it can never walk past the true option A into
    # stem text that merely happens to start with the same letter.
    # Page-break artifacts (stray page numbers, footer/header lines) can land
    # mid-list and must be dropped before line-based option detection, or
    # they break the strict sequential scan.
    lines = [l.strip() for l in stem_options_text.split("\n") if l.strip()]
    lines = [l for l in lines if not PAGE_NOISE_RE.match(l)]
    i = len(lines) - 1
    collected = []
    expected_next = None
    while i >= 0:
        om = OPTION_LINE_RE.match(lines[i])
        if not om:
            break
        letter = om.group(1)
        if expected_next is not None and ord(expected_next) - ord(letter) != 1:
            break
        collected.append((letter, om.group(2)))
        expected_next = letter
        i -= 1
        if letter == "A":
            break

    if collected and collected[-1][0] == "A":
        collected.reverse()
        options = {letter: clean(text) for letter, text in collected}
        question = clean(" ".join(lines[: i + 1]))
        return question, options

    # Occasionally the PDF extractor glues an option onto the end of the
    # stem's own line with no newline between them (e.g. "...the river
    # action? A River erosion"), so the backward scan above stops one letter
    # short. Try to recover that single missing letter from the tail of the
    # boundary line before giving up to the naive fallback.
    if collected:
        missing_letter = chr(ord(collected[-1][0]) - 1)
        boundary_idx = i
        if boundary_idx >= 0:
            boundary_line = lines[boundary_idx]
            m = re.search(r"(?:^|[.?!]\s+|\s)" + missing_letter + r"\s+([A-Z][^.?!]*)$", boundary_line)
            if m:
                collected.append((missing_letter, m.group(1)))
                if missing_letter == "A":
                    collected.reverse()
                    options = {letter: clean(text) for letter, text in collected}
                    question = clean(" ".join(lines[:boundary_idx]) + " " + boundary_line[: m.start()])
                    return question.strip(), options

    # fallback: no clean A..E/A..D run found ending at 'A' (rare/malformed
    # cases) - best effort forward scan
    options = {}
    question_lines = []
    for line in lines:
        om = OPTION_LINE_RE.match(line)
        if om and om.group(1) not in options:
            options[om.group(1)] = clean(om.group(2))
        else:
            question_lines.append(line)
    return clean(" ".join(question_lines)), options


def extract_answer_and_reason(explanation_text, options=None):
    """explanation_text = everything right after 'Answer:'/'Correct answer:', already
    bounded to end just before the next item's real marker. Handles three known styles:
      1. 'Answer: B Nephron' ... 'Reason: <text>'   (letter right after colon)
      2. 'Answer:\n<prose>\nThe correct answer is D (i) and (iv).'  (letter at the end)
      3. 'Correct answer: D do not bite... young mosquitoes. The passage states that...'
         (letter + restated option text run directly into the explanation with no
         separating keyword or newline - only a sentence-final period)

    A bare letter directly after 'Answer:' is only trusted if it's confirmed by
    matching the start of that letter's own known option text (or a 'Reason:'
    keyword is present). Otherwise it can be a false positive - e.g. explanation
    prose that happens to start with the word "A" ("A chemical change involves
    ...") - which would misidentify the answer. In that case 'The correct
    answer is X', when present, is authoritative and checked instead.
    """
    options = options or {}
    m_letter = re.match(r"\s*([A-E])\b\.?", explanation_text)
    reason_m = re.search(r"Reason\s*:\s*(.*)", explanation_text, re.DOTALL | re.IGNORECASE)

    letter_confirmed = False
    if m_letter:
        letter = m_letter.group(1)
        known_option_text = options.get(letter)
        if known_option_text:
            after = explanation_text[m_letter.end():].lstrip()
            norm_after = re.sub(r"\s+", " ", after).lower()
            norm_known = re.sub(r"\s+", " ", known_option_text).lower()
            letter_confirmed = norm_after.startswith(norm_known)
        if not letter_confirmed and reason_m:
            # the restated-option-text check can fail even for a genuine match
            # (e.g. "Answer: D\nReason: ..." with no restated text at all) - an
            # explicit 'Reason:' keyword is confirmation enough on its own
            letter_confirmed = True

    if letter_confirmed and reason_m:
        return m_letter.group(1), clean(reason_m.group(1))
    if letter_confirmed and not reason_m:
        letter = m_letter.group(1)
        after_letter = explanation_text[m_letter.end():]
        known_option_text = options.get(letter)
        if known_option_text:
            norm_after = re.sub(r"\s+", " ", after_letter).strip()
            norm_known = re.sub(r"\s+", " ", known_option_text).strip()
            remainder = norm_after[len(norm_known):].lstrip(" .")
            if remainder:
                return letter, clean(remainder)
        parts = after_letter.split("\n", 1)
        explanation = clean(parts[1]) if len(parts) > 1 else clean(after_letter)
        return letter, explanation

    ca_m = re.search(r"The correct answer is\s*([A-E])\b\.?\s*", explanation_text, re.IGNORECASE)
    if ca_m:
        return ca_m.group(1), clean(explanation_text[: ca_m.start()])

    # last resort: trust the unconfirmed bare letter if nothing else worked
    if m_letter:
        after_letter = explanation_text[m_letter.end():]
        parts = after_letter.split("\n", 1)
        explanation = clean(parts[1]) if len(parts) > 1 else clean(after_letter)
        explanation = re.sub(r"^Reason\s*:\s*", "", explanation, flags=re.IGNORECASE)
        return m_letter.group(1), explanation
    return None, None


def get_section_a_bounds(text):
    start_m = re.search(r"1\.\s*For each of the items.*?\n", text)
    if start_m:
        section_start = start_m.end()
    else:
        fallback_m = re.search(r"\(i\)\s+\S", text)
        if not fallback_m:
            return None
        section_start = fallback_m.start()
    end_m = re.search(r"\n\s*2\.\s", text[section_start:])
    section_end = section_start + end_m.start() if end_m else len(text)
    return section_start, section_end


def parse_section_a(text):
    bounds = get_section_a_bounds(text)
    if bounds is None:
        return []
    section_start, section_end = bounds

    items = []
    cursor = section_start
    while True:
        marker_m = MARKER_RE.search(text[cursor:section_end])
        if not marker_m:
            break
        roman = marker_m.group(1)
        marker_end = cursor + marker_m.end()

        am = ANCHOR_RE.search(text[marker_end:section_end])
        if not am:
            break
        am_start = marker_end + am.start()
        am_end = marker_end + am.end()

        stem_options_text = text[marker_end:am_start]
        question, options = parse_options(stem_options_text)

        am2 = ANCHOR_RE.search(text[am_end:section_end])
        if am2:
            am2_start = am_end + am2.start()
            search_zone = text[am_end:am2_start]
            next_markers = list(MARKER_RE.finditer(search_zone))
            if next_markers:
                # the LAST marker before the next item's own "Answer:" is that next
                # item's real outer marker; anything earlier in this zone is either
                # this item's own explanation text or a self-referential mention
                # (e.g. "The correct answer is D (i) and (iv).")
                cut = next_markers[-1].start()
                explanation_text = search_zone[:cut]
                cursor = am_end + cut
            else:
                explanation_text = search_zone
                cursor = am2_start
        else:
            explanation_text = text[am_end:section_end]
            cursor = section_end

        answer, reason = extract_answer_and_reason(explanation_text, options)
        if answer and question and len(options) >= 3:
            items.append({
                "marker": roman,
                "question": question,
                "options": options,
                "answer": answer,
                "reason": reason,
            })

        if not am2:
            break
    return items


if __name__ == "__main__":
    path = Path(sys.argv[1])
    text = get_text(path)
    items = parse_section_a(text)
    print(f"Parsed {len(items)} items from {path.name}")
    for it in items:
        print("----", it["marker"])
        print("Q:", it["question"])
        for k in "ABCDE":
            if k in it["options"]:
                print(f"  {k}: {it['options'][k]}")
        print("Answer:", it["answer"])
        print("Reason:", it["reason"])
