"""Download Form 3-4 past-paper PDFs from Maktaba by TETEA for selected subjects."""

import os
import re
from urllib.parse import unquote, urlparse

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://maktaba.tetea.org/resources/form-3-4/"
OUTPUT_DIR = "necta-papers"
SUBJECTS = ["Basic Maths", "Biology", "Chemistry", "English", "Geography", "History", "Civics"]

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) NectaScraper/1.0"}


def slugify(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def find_subject_table(soup, subject_name):
    """Return the <table> element following the <h3> heading for subject_name."""
    for h3 in soup.select("div.entry-content h3"):
        heading_text = h3.get_text().replace("(back to top)", "").strip()
        if heading_text.lower() == subject_name.lower():
            table = h3.find_next_sibling("table")
            return table
    return None


def download_pdf(url, dest_path):
    response = requests.get(url, headers=HEADERS, timeout=60)
    response.raise_for_status()
    with open(dest_path, "wb") as f:
        f.write(response.content)


def main():
    print(f"Fetching {BASE_URL} ...")
    resp = requests.get(BASE_URL, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    summary = {}

    for subject in SUBJECTS:
        table = find_subject_table(soup, subject)
        if table is None:
            print(f"WARNING: could not find section for subject '{subject}'")
            summary[subject] = {"downloaded": 0, "skipped": 0, "failed": 0}
            continue

        subject_dir = os.path.join(OUTPUT_DIR, slugify(subject))
        os.makedirs(subject_dir, exist_ok=True)

        pdf_links = [a["href"] for a in table.find_all("a", href=True) if a["href"].lower().endswith(".pdf")]

        downloaded = skipped = failed = 0

        for link in pdf_links:
            filename = unquote(os.path.basename(urlparse(link).path))
            dest_path = os.path.join(subject_dir, filename)

            if os.path.exists(dest_path):
                skipped += 1
                continue

            try:
                print(f"  [{subject}] downloading {filename} ...")
                download_pdf(link, dest_path)
                downloaded += 1
            except requests.RequestException as e:
                print(f"  [{subject}] FAILED: {filename} ({e})")
                failed += 1

        summary[subject] = {"downloaded": downloaded, "skipped": skipped, "failed": failed}

    print("\n=== Summary ===")
    total_downloaded = 0
    for subject, stats in summary.items():
        print(
            f"{subject}: {stats['downloaded']} downloaded, "
            f"{stats['skipped']} skipped (already existed), {stats['failed']} failed"
        )
        total_downloaded += stats["downloaded"]
    print(f"\nTotal new files downloaded: {total_downloaded}")


if __name__ == "__main__":
    main()
