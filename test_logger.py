# test_logger.py

from utils.task_logger import log_task
from utils.csv_loader import load_user_config

log_task("login", "success", "Cookies used from file")
log_task("apply_job", "failed", "Job already applied")

config = load_user_config()
print(config)