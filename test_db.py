# test_db.py

from state.db_manager import DBManager

db = DBManager()
db.log_task_run("daily_post", "success", "Post published")
db.log_task_run("apply_jobs", "failure", "Login expired")
rows = db.fetch_all_runs()

print("📄 All task logs:")
for row in rows:
    print(row)

db.close()