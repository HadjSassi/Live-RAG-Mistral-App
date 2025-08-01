import requests
from config.env import MISTRAL_API_KEY, ENDPOINT

def format_prompt(context, question):
    return [
        {"role": "system", "content": "You are a helpful assistant. Answer the question based only on the context. Toujours en francais"},
        {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}"}
    ]

def get_mistral_response(context, question):
    messages = format_prompt(context, question)
    answer = query_mistral(messages)
    print("\n🤖 Réponse Mistral :\n", answer)

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
