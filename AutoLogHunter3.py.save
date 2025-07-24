import argparse
import re
import sqlite3
import time
from datetime import datetime
from collections import defaultdict

# --------------------------
# Argument Parser
# --------------------------
def parse_arguments():
    parser = argparse.ArgumentParser(description='AutoLogHunter - Enhanced log analysis tool.')
    parser.add_argument('-l', '--log', required=True, help='Path to the log file')
    parser.add_argument('-k', '--keywords', nargs='+', help='Keywords to search for (e.g., "Failed password")')
    parser.add_argument('-r', '--realtime', action='store_true', help='Enable real-time log monitoring')
    return parser.parse_args()

# --------------------------
# Severity Tagging
# --------------------------
def tag_severity(line):
    if 'failed password' in line.lower():
        return 'CRITICAL'
    elif 'invalid user' in line.lower():
        return 'WARNING'
    elif 'session opened' in line.lower() or 'accepted password' in line.lower():
        return 'INFO'
    else:
        return 'UNKNOWN'

# --------------------------
# IP Extraction + Scoring
# --------------------------
ip_counter = defaultdict(int)
THRESHOLD = 5

def extract_ip(line):
    match = re.search(r'(\d{1,3}(?:\.\d{1,3}){3})', line)
    return match.group(1) if match else None

def update_ip_score(ip):
    ip_counter[ip] += 1
    if ip_counter[ip] > THRESHOLD:
        print(f"[!] Brute-force suspected from IP: {ip} ({ip_counter[ip]} attempts)")

# --------------------------
# SQLite Storage
# --------------------------
def init_db():
    conn = sqlite3.connect('autologhunter.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            ip TEXT,
            severity TEXT,
            message TEXT
        )
    ''')
    conn.commit()
    return conn

def insert_log(conn, timestamp, ip, severity, message):
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO logs (timestamp, ip, severity, message) VALUES (?, ?, ?, ?)',
        (timestamp, ip, severity, message)
    )
    conn.commit()

# --------------------------
# Log Analysis
# --------------------------
def process_log_line(line, keywords, conn):
    if any(keyword.lower() in line.lower() for keyword in keywords):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ip = extract_ip(line)
        severity = tag_severity(line)
        clean_line = line.strip()

        if ip:
            update_ip_score(ip)
        insert_log(conn, timestamp, ip, severity, clean_line)

        print(f"[{severity}] {timestamp} | {ip or 'No IP'} | {clean_line}")

# --------------------------
# Real-time Monitoring
# --------------------------
def tail_log_file(filepath, keywords, conn):
    with open(filepath, 'r') as file:
        file.seek(0, 2)  # Go to EOF
        while True:
            line = file.readline()
            if not line:
                time.sleep(0.5)
                continue
            process_log_line(line, keywords, conn)

# --------------------------
# Main Runner
# --------------------------
def main():
    args = parse_arguments()
    conn = init_db()

    if args.realtime:
        print("[*] Starting real-time monitoring...\n")
        tail_log_file(args.log, args.keywords, conn)
    else:
        try:
            with open(args.log, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    process_log_line(line, args.keywords, conn)
        except FileNotFoundError:
            print(f"[!] Log file not found: {args.log}")
            exit(1)

    conn.close()

if __name__ == '__main__':
    main()

