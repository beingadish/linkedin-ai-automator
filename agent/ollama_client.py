import requests
from config import settings

def query_ollama(prompt: str) -> str:
    url = f"{settings.OLLAMA_HOST}/api/generate"
    data = {
        "model": settings.OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        return response.json()["response"]
    return f"Error: {response.status_code} {response.text}"
