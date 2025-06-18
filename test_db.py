from state.db_manager import DBManager

# Directly use the database path
db = DBManager("state/user_state.db")

# Simulate running a task
db.update_task_timestamp("daily_post")

# Fetch last run time of the task
last_run = db.get_last_run("daily_post")
print(f"Last run time for daily_post: {last_run}")
