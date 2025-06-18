# test_session.py
import asyncio
from browser.session_manager import BrowserSessionManager
from browser.dom_snapshot import save_dom_snapshot

async def test():
    manager = BrowserSessionManager()
    await manager.launch()
    page = await manager.new_page("https://www.linkedin.com/feed/")

    print("👉 Please login manually, then press ENTER here to continue...")
    input()

    await manager.save_cookies()
    await save_dom_snapshot(page)
    await manager.close()

asyncio.run(test())