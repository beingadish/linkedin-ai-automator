from dotenv import load_dotenv
import os

load_dotenv()

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")
OLLAMA_HOST = os.getenv("OLLAMA_HOST")
USER_CONFIG_CSV = os.getenv("USER_CONFIG_CSV")
TASK_LOG_CSV = os.getenv("TASK_LOG_CSV")
SQLITE_DB_PATH = os.getenv("SQLITE_DB_PATH")
COOKIES_PATH = os.getenv("COOKIES_PATH")