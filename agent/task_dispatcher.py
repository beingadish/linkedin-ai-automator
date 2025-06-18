from tasks.daily_post import run_post_task
from tasks.apply_jobs import run_job_apply
from tasks.connect_people import run_connect
from tasks.comment_trending import run_comment
from tasks.read_inbox import run_read_inbox

def dispatch_task(task: str):
    if task == "post":
        run_post_task()
    elif task == "apply_job":
        run_job_apply()
    elif task == "connect":
        run_connect()
    elif task == "comment":
        run_comment()
    elif task == "read_inbox":
        run_read_inbox()
    else:
        print(f"Unknown task: {task}")
