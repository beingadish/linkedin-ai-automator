from state.task_logger import TaskLogger

logger = TaskLogger()

# Simulate log entry
logger.log("daily_post", "success", "Posted motivational quote")
logger.log("apply_jobs", "failure", "No matching jobs found")

print("Logs written to data/task_log.csv")
