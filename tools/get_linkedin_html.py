from langchain_core.tools import tool
from browser.session_manager import BrowserSessionManager

@tool("get_linkedin_html")
async def get_linkedin_html(dummy_input: str) -> str:
    """Fetch the raw LinkedIn homepage HTML. Use this to analyze the page structure or extract information."""
    print("[TOOL] get_linkedin_html running")
    manager = BrowserSessionManager()
    await manager.launch()
    page = await manager.new_page("https://www.linkedin.com/feed/")
    await page.wait_for_timeout(5000)  # wait for content to settle
    html = await page.content()
    await manager.close()
    return html
