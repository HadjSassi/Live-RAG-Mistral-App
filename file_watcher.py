# handles new files
# file_watcher.py
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

from embedder import chunk_text, embed_chunks
from qdrant_utils import add_documents

def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

class NewFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith(".txt"):
            print(f"📄 New file detected: {event.src_path}")
            text = read_file(event.src_path)
            metadata = {"source": os.path.basename(event.src_path)}
            chunks = chunk_text(text, metadata)
            vectors, metas = embed_chunks(chunks)
            add_documents(vectors, metas)
            print(f"✅ Indexed {len(chunks)} chunks from {event.src_path}")

def start_watching(folder="documents"):
    observer = Observer()
    observer.schedule(NewFileHandler(), path=folder, recursive=False)
    observer.start()
    print(f"👀 Watching folder: {folder}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
