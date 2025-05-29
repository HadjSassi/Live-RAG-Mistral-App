import requests
from env import MISTRAL_API_KEY, ENDPOINT

def query_mistral(messages):
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistral-medium",  # or "mistral-small", "mistral-tiny"
        "messages": messages,
        "temperature": 0.7
    }

    response = requests.post(ENDPOINT, headers=headers, json=data)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
