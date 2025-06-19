from langchain_core.tools import tool
from browser.session_manager import BrowserSessionManager

@tool("get_username_tool")
async def get_username_tool(dummy_input: str) -> str:
    print("[DEBUG] get_username_tool called")  # Add this line
    """Fetch the LinkedIn display name from the homepage. Use this tool whenever the user asks for their LinkedIn name, profile name, or display name."""
    manager = BrowserSessionManager()
    await manager.launch()
    page = await manager.new_page("https://www.linkedin.com/feed/")

    # Take a screenshot for debugging
    await page.screenshot(path="linkedin_debug.png")
    print("[DEBUG] Screenshot saved as linkedin_debug.png")

    # Save the HTML content for debugging
    html_content = await page.content()
    with open("linkedin_debug.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("[DEBUG] HTML content saved as linkedin_debug.html")

    # Try multiple selectors for robustness
    selectors = [
        "div.feed-identity-module__actor-meta span",
        "div.feed-identity-module__actor-meta span[aria-hidden='false']",
        "div.feed-identity-module__member-name span",
        "span.text-heading-xlarge",  # Sometimes used for profile name
    ]
    name = None
    for selector in selectors:
        try:
            await page.wait_for_selector(selector, timeout=1000)  # 1 second timeout
            name_element = await page.query_selector(selector)
            if name_element:
                name = await name_element.inner_text()
                print(f"[DEBUG] Found name with selector '{selector}': {name}")
                if name and name.strip():
                    break
        except Exception as e:
            print(f"[DEBUG] Selector '{selector}' failed: {e}")
            continue

    await manager.close()
    return name.strip() if name else "Name not found"
