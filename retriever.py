# search & retrieve top docs
# retriever.py

from qdrant_client import QdrantClient
from embedder import embed_text
from qdrant_utils import COLLECTION_NAME
from env import HOST, PORT

client = QdrantClient(HOST, port=PORT)

def get_relevant_chunks(query, top_k=5):
    query_vector = embed_text(query)
    hits = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_vector,
        limit=top_k
    )
    return [{"text": hit.payload["text"], "score": hit.score} for hit in hits]

