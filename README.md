# AutoLogHunter-Python-Scripting-
AutoLogHunter is my first independent cybersecurity scripting project. I built this tool to improve my understanding of log analysis, Linux system behavior, and real-world threat detection techniques relevant to cybersecurity defense.

This Python script parses system log files and identifies potentially suspicious activities such as brute-force login attempts, SSH authentication failures, and login anomalies. Alerts are displayed on the console and optionally saved to an output file.

🔍 Key Features:

- Parses custom or system log files (test.log)

Detects:

    - Failed SSH login attempts

    - Brute-force behavior from suspcious IPs

    - Invalid user logins

    - Supports keyword-based scanning

My Setup & Roadblocks:

While setting this project up, I used a Kali Linux VM running in Oracle VirtualBox. Initially, I intended to parse /var/log/auth.log, which logs authentication attempts. However, I found the file was either missing or inaccessible due to logging not being enabled by default.

Since I'm working on a MacBook, I couldn't access /var/log/auth.log there either — macOS uses a unified log system that doesn't expose these logs in plain text. To move forward, I simulated log entries in a test file.

Logs host authentication events are triggered by users that attempt to access resources.


⚙️ Setup Instructions: 

1. To Open Terminal press "cmmd + spacebar" and search terminal and open it 

2. Create a Working Directory with commands:
    cd ~
    mkdir AutoLogHunter // make new directory
    cd AutoLogHunter // change into direcory

3. Create the Python Script:
    nano autologhunter.py

4. Create a Fake Test Log File since auth.logs cannot be accessed:
    "May 27 18:01:03 server sshd[1234]: Failed password for invalid user root from 192.168.1.12"
    "May 27 18:02:45 server sshd[1235]: Failed password for invalid user admin from 192.168.1.14"
    "May 27 18:07:10 server sshd[1236]: Accepted password for user marcus from 192.168.1.10 port 22 ssh2"
    "May 27 18:10:00 server login[5678]: login failure for user test from 192.168.1.20"

5. 