# agent/task_dispatcher.py

import importlib

class TaskDispatcher:
    def __init__(self):
        self.task_map = {
            "apply_jobs": "tasks.apply_jobs",
            "comment_post": "tasks.comment_trending",
            "connect_people": "tasks.connect_people",
            "daily_post": "tasks.daily_post",
            "read_inbox": "tasks.read_inbox",
        }

    async def dispatch(self, task_name: str, context: dict):
        """
        Given a task name and context, run the associated task.
        """
        if task_name not in self.task_map:
            raise ValueError(f"[Dispatcher] Task '{task_name}' not recognized.")

        module_name = self.task_map[task_name]
        module = importlib.import_module(module_name)

        if not hasattr(module, "run"):
            raise AttributeError(f"[Dispatcher] Module '{module_name}' must have a 'run' function.")

        return await module.run(context)
