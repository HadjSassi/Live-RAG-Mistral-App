# CLI & main logic
from utils.rag.qdrant_utils import init_qdrant
from utils.rag.file_watcher import start_watching

if __name__ == "__main__":
    print("🚀 Starting RAG Live App")
    init_qdrant()
    start_watching("documents")