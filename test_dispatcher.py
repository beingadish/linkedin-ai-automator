# test_dispatcher.py

import asyncio
from agent.task_dispatcher import TaskDispatcher

async def test():
    dispatcher = TaskDispatcher()
    await dispatcher.dispatch("daily_post", {"dummy": "data"})

if __name__ == "__main__":
    asyncio.run(test())
