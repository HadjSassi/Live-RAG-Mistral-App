import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.rag.file_watcher import start_watching
from utils.rag.qdrant_utils import init_qdrant

init_qdrant()
start_watching("documents")