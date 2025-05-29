from query_mistral import query_mistral
question = "Who is Alan Turing?"
context = "Alan Turing was a British mathematician and computer scientist..."

messages = [
    {"role": "system", "content": "You are a helpful assistant that answers questions based on context."},
    {"role": "user", "content": f"Context: {context}\n\nQuestion: {question}"}
]

answer = query_mistral(messages)
print("🤖 Mistral says:", answer)
