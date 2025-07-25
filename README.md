# 🔍 AutoLogHunter3

AutoLogHunter3 is a real-time Linux log monitoring and anomaly detection tool written in Python. It’s built to identify suspicious authentication behavior, tag severity levels, score IP activity, and visualize flagged events through a live dashboard.

> Built to grow with me as I grow as a cybersecurity engineer.

---

## 🚀 Features

- 📡 **Real-Time Log Monitoring** (`tail -f` style)
- 🛑 **Severity Tagging** (INFO, WARNING, CRITICAL)
- 🔐 **Brute-Force Detection** via IP scoring
- 💾 **Persistent Event Storage** (SQLite)
- 🌐 **Flask Dashboard** to visualize and review events
- 🧪 **Test Log Parser** that mimics `/var/log/auth.log`

---

## 🧠 Problems I Faced + Lessons Learned

| Challenge | Solution |
|----------|-----------|
| Dashboard wouldn’t load results | Learned I needed to actually trigger log events with matching keywords to create the `logs` table |
| Got `no such table: logs` errors | Realized the database file was created before `init_db()` existed — fixed by deleting `.db` and re-running |
| Log test cases weren't realistic | Replaced hardcoded tags with real-looking syslog-style lines |
| Confused about how updates overwrite the README | Learned that Git keeps history of all commits and README versions |

---

## 🧱 Architecture Overview

```plaintext
AutoLogHunter3.py         # CLI log scanner + DB writer
dashboard.py              # Flask dashboard for results
templates/dashboard.html  # UI for event review
test.log                  # Sample logs for testing
autologhunter.db          # SQLite storage (created on first run)

