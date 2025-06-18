import sqlite3
from datetime import datetime

class DBManager:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self._create_table()

    def _create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS task_state (
            task_name TEXT PRIMARY KEY,
            last_run TIMESTAMP
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def update_task_timestamp(self, task_name: str):
        now = datetime.now().isoformat()
        query = """
        INSERT INTO task_state (task_name, last_run)
        VALUES (?, ?)
        ON CONFLICT(task_name) DO UPDATE SET last_run=excluded.last_run
        """
        self.conn.execute(query, (task_name, now))
        self.conn.commit()

    def get_last_run(self, task_name: str) -> str:
        query = "SELECT last_run FROM task_state WHERE task_name = ?"
        cursor = self.conn.execute(query, (task_name,))
        row = cursor.fetchone()
        return row[0] if row else None
