import os

BASE_DIR = os.getcwd()

UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

CHROMA_DIR = os.path.join(BASE_DIR, "chroma_db")

COLLECTION_NAME = "pdf_rag_collection"

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

AVAILABLE_MODELS = [
    "gemma3:1b",
    "gemma3:latest",
]

DEFAULT_MODEL = "gemma3:1b"
OLLAMA_MODEL = DEFAULT_MODEL

TOP_K = 4

OLLAMA_BASE_URL = "http://localhost:11434"