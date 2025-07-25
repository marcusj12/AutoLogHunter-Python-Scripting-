# 🔍 AutoLogHunter3 – Real-Time Linux Log Anomaly Detector

AutoLogHunter3 is a Python-based security log monitoring tool designed to simulate core functionality of a lightweight SOC (Security Operations Center) utility. It allows detection of brute-force attacks and other suspicious login activities in real time, supports log tagging, persistent storage, and visual reporting via a Flask dashboard.

---

## 🎯 Recruiter Summary

> This project simulates a lightweight SOC tool developed using Python.
>
> **AutoLogHunter3** was created to:
>
> * Detect brute-force login attempts in real time
> * Tag and prioritize auth activity (INFO, WARNING, CRITICAL)
> * Store logs persistently using SQLite
> * Visualize anomalies with a Flask web dashboard
> * Prepare for deployment on real Linux log environments (e.g., Splunk, syslog)

It demonstrates skills in:

* Python scripting
* Regex & keyword detection
* Real-time log tailing
* SQLite database integration
* Flask web development
* Cybersecurity workflows and detection thinking

---

## 🧭 Project Evolution

* **v1.0**: Initial release with basic keyword-based detection
* **v1.1**: Added real-time monitoring, IP scoring, severity tagging, and SQLite logging
* **v2.0**: Introduced Flask dashboard, modular architecture, and realistic log simulations
* **v3.0 (planned)**: Regex detection, GeoIP mapping, exportable reports, full GUI, and live log integration

---

## 📦 Features (v2)

* ✅ Real-time log monitoring (`--realtime` flag)
* ✅ Severity tagging: INFO, WARNING, CRITICAL
* ✅ IP scoring to detect brute-force attempts
* ✅ Persistent SQLite storage
* ✅ Flask dashboard for anomaly visualization
* ✅ Structured, modular code design

---

## 🧪 Example Use

```bash
python3 AutoLogHunter3.py -l test.log -k "Failed password" "Invalid user"
```

For real-time monitoring:

```bash
python3 AutoLogHunter3.py -l /var/log/auth.log -k "Failed password" "Invalid user" --realtime
```

To view the dashboard:

```bash
python3 dashboard.py
```

Visit `http://localhost:5000` in your browser.

---

## 🧠 Lessons Learned

| Lesson                                   | Insight                                                                                                                  |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| 💥 Debugging isn’t always about the code | Some issues stemmed from test data and understanding how logs trigger behavior, not just the Python logic                |
| 🧩 Understanding Git matters             | Merge conflicts and local vs remote branch issues forced me to learn how to properly resolve version control problems    |
| 🗃️ Test data is critical                | Without real-looking logs, it was hard to validate the tool’s logic. Creating authentic log lines solved visibility bugs |
| 🏗️ Code structure is power              | Modularizing parsing, storage, and UI made debugging and building easier                                                 |
| 🧪 Break it to fix it                    | Every failure deepened my understanding of how systems interact, from DB schema to CLI tooling                           |
| 🧭 Projects evolve                       | Starting small helped me stay focused while scaling the tool toward production-like readiness                            |

---

## 📌 Planned Features for v3

* 📤 Export anomalies to `.csv` or `.txt` report
* 🌍 GeoIP lookup for suspicious IPs
* 🧬 Regex-based detection engine (not just keywords)
* 🖥️ Full GUI using Tkinter or Flask enhancements
* 📡 Integration with live server logs (e.g., Splunk, journald)

---

## 🚀 Setup

```bash
pip install flask
```

Ensure your environment is using Python 3.8+ and that `autologhunter.db` is writable.

---

## 🧾 GitHub Releases

### 🔖 v1.1 – Core Detection Engine

* Introduced real-time log monitoring
* Added severity tagging and IP scoring
* Built lightweight Flask dashboard
* Fixed database initialization issues

### 🧪 v2 – Modular Detection + Web Visualization

* Refactored to structured, maintainable modules
* Simulated production-level threat detection
* Added recruiter-facing documentation

---

## 🤝 Feedback / Collaboration

If you work in SOC, detection engineering, or threat hunting — I’d love your feedback.

Pull requests and contributions are welcome.

> Built with Python, sweat, and curiosity.

