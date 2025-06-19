from langchain_core.tools import tool
from browser.session_manager import BrowserSessionManager
import asyncio

def _get_username_sync(dummy_input: str) -> str:
    async def inner():
        print("[TOOL] get_username_tool running (sync)")
        manager = BrowserSessionManager()
        await manager.launch()
        page = await manager.new_page("https://www.linkedin.com/feed/")

        await page.screenshot(path="linkedin_debug.png")
        html = await page.content()
        with open("linkedin_debug.html", "w", encoding="utf-8") as f:
            f.write(html)

        selectors = [
            "div.feed-identity-module__actor-meta span",
            "div.feed-identity-module__actor-meta span[aria-hidden='false']",
            "div.feed-identity-module__member-name span",
            "span.text-heading-xlarge",
        ]
        for selector in selectors:
            try:
                await page.wait_for_selector(selector, timeout=10000)
                name_el = await page.query_selector(selector)
                if name_el:
                    name = await name_el.inner_text()
                    if name.strip():
                        await manager.close()
                        return name.strip()
            except Exception as e:
                print(f"[TOOL] Failed on selector {selector}: {e}")
                continue

        await manager.close()
        return "Name not found"

    return asyncio.run(inner())

@tool("get_username_tool")
def get_username_tool(dummy_input: str) -> str:
    """Fetch the LinkedIn display name from the homepage (sync wrapper)."""
    return _get_username_sync(dummy_input)