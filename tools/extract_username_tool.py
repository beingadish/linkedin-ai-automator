from langchain_core.tools import tool

@tool("extract_username_from_html")
def extract_username_tool(html: str) -> str:
    """Extract LinkedIn display name from the homepage HTML."""
    return html  # LLM interprets this and extracts the name
