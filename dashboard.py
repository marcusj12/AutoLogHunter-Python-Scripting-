from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('autologhunter.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def dashboard():
    conn = get_db_connection()

    # Get most recent logs
    logs = conn.execute('''
        SELECT * FROM logs
        ORDER BY id DESC
        LIMIT 20
    ''').fetchall()

    # Get top brute-force IPs
    top_ips = conn.execute('''
        SELECT ip, COUNT(*) as count
        FROM logs
        WHERE severity = 'CRITICAL' AND ip IS NOT NULL
        GROUP BY ip
        ORDER BY count DESC
        LIMIT 5
    ''').fetchall()

    conn.close()
    return render_template('dashboard.html', logs=logs, top_ips=top_ips)

if __name__ == '__main__':
    app.run(debug=True)

