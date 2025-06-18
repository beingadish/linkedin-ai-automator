# config/settings.py
from dotenv import load_dotenv
import os

# Load environment variables from `.env`
load_dotenv()

# Access them with defaults if not present
DEBUG_MODE = os.getenv("DEBUG_MODE", "true").lower() == "true"
BROWSER_TYPE = os.getenv("BROWSER_TYPE", "chromium")
BROWSER_USE_HEADLESS = os.getenv("BROWSER_USE_HEADLESS", "false").lower() == "true"
BROWSER_USE_VISIBLE = os.getenv("BROWSER_USE_VISIBLE", "true").lower() == "true"
LINKEDIN_START_URL = os.getenv("LINKEDIN_START_URL")

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")
OLLAMA_HOST = os.getenv("OLLAMA_HOST")

USER_CONFIG_CSV = os.getenv("USER_CONFIG_CSV")
TASK_LOG_CSV = os.getenv("TASK_LOG_CSV")
SQLITE_DB_PATH = os.getenv("SQLITE_DB_PATH")
COOKIES_PATH = os.getenv("COOKIES_PATH")
