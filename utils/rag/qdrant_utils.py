# vector db interaction
# qdrant_client.py
from uuid import uuid4

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from config.env import COLLECTION_NAME,VECTOR_SIZE, HOST, PORT

client = QdrantClient(host= HOST, port= PORT)

def init_qdrant():
    if COLLECTION_NAME not in client.get_collections().collections:
        client.recreate_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=VECTOR_SIZE, distance=Distance.COSINE)
        )
    print(f"✅ Qdrant collection '{COLLECTION_NAME}' ready.")

def add_documents(vectors, metas):
    if not vectors:
        print("⚠️ No vectors to add. Skipping upsert.")
        return

    print(f"📌 Adding {len(vectors)} vectors to Qdrant")

    points = [
        PointStruct(
            id=uuid4().int >> 64,
            vector=vector,
            payload=meta
        )
        for vector, meta in zip(vectors, metas)
    ]
    client.upsert(collection_name=COLLECTION_NAME, points=points)