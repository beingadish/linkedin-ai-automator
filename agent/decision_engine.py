from agent.ollama_client import query_ollama

def get_next_task(context: str) -> str:
    prompt = f"""
You are an automation agent. Given the current LinkedIn user context:
\"\"\"
{context}
\"\"\"
Decide what task should be performed next: 
[post, apply_job, connect, comment, read_inbox]
Only return the task keyword.
"""
    return query_ollama(prompt).strip().lower()
