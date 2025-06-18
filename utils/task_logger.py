# utils/task_logger.py

import csv
from datetime import datetime
from pathlib import Path

LOG_PATH = Path("data/task_log.csv")

def log_task(action: str, status: str, details: str = ""):
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    is_new_file = not LOG_PATH.exists()

    with open(LOG_PATH, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if is_new_file:
            writer.writerow(["timestamp", "action", "status", "details"])
        writer.writerow([datetime.now().isoformat(), action, status, details])
