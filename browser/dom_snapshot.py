# browser/dom_snapshot.py
from pathlib import Path

async def save_dom_snapshot(page, filename="linkedin_snapshot.html"):
    html_content = await page.content()
    path = Path("state") / filename
    path.write_text(html_content, encoding="utf-8")
    print(f"[Snapshot] ✅ Saved DOM snapshot to {path}")

    # Optional: also save a screenshot
    screenshot_path = Path("state") / "linkedin_snapshot.png"
    await page.screenshot(path=screenshot_path, full_page=True)
    print(f"[Snapshot] 🖼️ Screenshot saved to {screenshot_path}")
