import csv
import os
from datetime import datetime

class TaskLogger:
    def __init__(self, log_file: str = "data/task_log.csv"):
        self.log_file = log_file
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        if not os.path.exists(self.log_file):
            with open(self.log_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["timestamp", "task_name", "status", "details"])

    def log(self, task_name: str, status: str, details: str = ""):
        timestamp = datetime.utcnow().isoformat()
        with open(self.log_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, task_name, status, details])
