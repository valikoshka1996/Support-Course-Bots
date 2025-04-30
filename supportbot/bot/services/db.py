import sqlite3
from datetime import datetime

async def log_request(user_id, message):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            message TEXT,
            created_at TEXT
        )
    """)
    c.execute("INSERT INTO requests (user_id, message, created_at) VALUES (?, ?, ?)",
              (user_id, message, datetime.now().isoformat()))
    conn.commit()
    conn.close()
