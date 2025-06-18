# utils/csv_loader.py

import csv
from pathlib import Path

CONFIG_PATH = Path("data/user_config.csv")

def load_user_config():
    if not CONFIG_PATH.exists():
        raise FileNotFoundError(f"Missing config file: {CONFIG_PATH}")

    with open(CONFIG_PATH, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)
