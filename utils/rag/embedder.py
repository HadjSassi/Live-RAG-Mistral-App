# loads and embeds chunks
# embedder.py

from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
embedder = SentenceTransformer("all-MiniLM-L6-v2")

def chunk_text(text, metadata):
    chunks = splitter.split_text(text)
    return [{"text": c, "metadata": {**metadata, "chunk": i, "text": c}} for i, c in enumerate(chunks)]

def embed_chunks(chunks):
    texts = [c["text"] for c in chunks]
    embeddings = embedder.encode(texts).tolist()
    metadatas = [c["metadata"] for c in chunks]
    return embeddings, metadatas

def embed_text(text):
    return embedder.encode(text).tolist()
