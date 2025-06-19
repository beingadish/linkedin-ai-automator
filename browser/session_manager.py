# browser/session_manager.py

import asyncio
import json
from pathlib import Path
from playwright.async_api import async_playwright

COOKIES_PATH = "state/linkedin_cookies.json"

class BrowserSessionManager:
    def __init__(self):
        self.browser = None
        self.context = None
        self.page = None
        self.playwright = None

    async def launch(self):
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=False)
        self.context = await self.browser.new_context()
        self.page = await self.context.new_page()

        # Step 1: Navigate to LinkedIn base to allow setting cookies
        await self.page.goto("https://www.linkedin.com")
        
        # Step 2: Load cookies if available
        cookie_path = Path(COOKIES_PATH)
        if cookie_path.exists():
            cookies = json.loads(cookie_path.read_text())
            await self.context.add_cookies(cookies)
            print("[Session] ✅ Cookies loaded")

        return self.page

    async def new_page(self, url: str):
        if not self.page:
            await self.launch()
        await self.page.goto(url)
        return self.page

    async def save_cookies(self):
        cookies = await self.context.cookies()
        Path("state").mkdir(parents=True, exist_ok=True)
        Path(COOKIES_PATH).write_text(json.dumps(cookies, indent=2))
        print(f"[Session] ✅ Cookies saved to {COOKIES_PATH}")

    async def close(self):
        if self.browser:
            await self.browser.close()
        if self.playwright:
            await self.playwright.stop()