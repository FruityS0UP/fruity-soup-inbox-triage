# Fruity Soup — Inbox Triage + Summarizer 🍲📬
![License: All Rights Reserved](https://img.shields.io/badge/license-All%20Rights%20Reserved-red)

> Local-first agent that categorizes emails, flags urgent ones, and generates a daily HTML digest with suggested replies.

---

## ✨ Features
- Categorization: **Billing, Support, Sales, Marketing, Personal, Spam**
- Urgency detection (keywords like “urgent”, “asap”, “past due”)
- 1–3 bullet summaries per message + suggested reply drafts
- Clean daily digest: counts, top category, per-category sections
- Runs **locally** — your data stays on your machine

---

## 🛠 Quickstart
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python agent.py data/sample_emails.json
# -> open reports/daily_summary.html

