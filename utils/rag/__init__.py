from utils.rag.query_mistral import get_mistral_response
from utils.rag.retriever import get_relevant_chunks


def handle_contextual_query(question):
    print("📚 Recherche contextuelle en cours...")
    chunks = get_relevant_chunks(question, top_k=10)
    context = "\n---\n".join([chunk['text'] for chunk in chunks])
    get_mistral_response(context, question)