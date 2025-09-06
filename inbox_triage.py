#!/usr/bin/env python3
# Fruity Soup License – All Rights Reserved
# Copyright © 2025 Fruity Soup
# Published for demonstration purposes only.

import sys
import json
from pathlib import Path

from utils.classify import classify_emails
from utils.summarize import summarize_emails
from utils.report import render_report

def main():
    if len(sys.argv) < 2:
        print("Usage: python agent.py data/sample_emails.json")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    if not input_path.exists():
        print(f"Input not found: {input_path}")
        sys.exit(1)

    #  Load raw emails (JSON array with fields: id, date, from's, to's, subject, body) All the email goods
    with open(input_path, "r", encoding="utf-8") as f:
        emails = json.load(f)

    #  Categorize + urgency scoring (pushing the important to the front of the line)
    triaged, counts = classify_emails(emails)

    #  Summarize + prepare suggested replies per message
    summaries = summarize_emails(triaged)

    #  Render daily digest HTML for easy reading
    out_dir = Path("reports")
    out_dir.mkdir(exist_ok=True)
    html_path = render_report(summaries, counts, out_dir)

    print(f"✅ Daily digest generated: {html_path}")

if __name__ == "__main__":
    main()

# Created By Jevante Boxley
