# state/db_manager.py

import sqlite3
from datetime import datetime
from pathlib import Path

DB_PATH = "state/user_state.db"

class DBManager:
    def __init__(self, db_path=DB_PATH):
        Path("state").mkdir(exist_ok=True)
        self.conn = sqlite3.connect(db_path)
        self._create_table()

    def _create_table(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS task_runs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task_name TEXT,
                    run_time TEXT,
                    status TEXT,
                    details TEXT
                );
            """)

    def log_task_run(self, task_name, status, details=""):
        now = datetime.utcnow().isoformat()
        with self.conn:
            self.conn.execute("""
                INSERT INTO task_runs (task_name, run_time, status, details)
                VALUES (?, ?, ?, ?)
            """, (task_name, now, status, details))
        print(f"[DB] ✅ Logged task: {task_name} [{status}]")

    def fetch_all_runs(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM task_runs")
        return cursor.fetchall()

    def close(self):
        self.conn.close()