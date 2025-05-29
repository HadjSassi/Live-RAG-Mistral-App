# query.py

from retriever import get_relevant_chunks
from query_mistral import query_mistral

def format_prompt(context, question):
    return [
        {"role": "system", "content": "You are a helpful assistant. Answer the question based only on the context."},
        {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}"}
    ]

def main():
    question = input("❓ Ask a question: ")

    chunks = get_relevant_chunks(question, top_k=5)
    context = "\n---\n".join([chunk['text'] for chunk in chunks])

    messages = format_prompt(context, question)
    answer = query_mistral(messages)

    print("\n🤖 Mistral's Answer:\n", answer)

if __name__ == "__main__":
    main()
