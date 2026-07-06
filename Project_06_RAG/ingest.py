"""
ingest.py
---------
Everything related to turning a raw PDF file into searchable vectors:

    PDF file -> pages -> chunks -> embeddings -> ChromaDB

Each function does exactly one job so the pipeline is easy to follow
and easy to test on its own.
"""

import shutil

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# LangChain has reorganized these into standalone packages over time.
# Try the modern import first, fall back to the older community one so the
# app keeps working regardless of which version is installed.
try:
    from langchain_huggingface import HuggingFaceEmbeddings
except ImportError:  # pragma: no cover
    from langchain_community.embeddings import HuggingFaceEmbeddings

try:
    from langchain_chroma import Chroma
except ImportError:  # pragma: no cover
    from langchain_community.vectorstores import Chroma

import config


def load_pdf(pdf_path: str):
    """Load a PDF from disk and return one LangChain Document per page."""
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()
    return pages


def split_documents(pages):
    """Split pages into overlapping chunks for better retrieval quality."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.CHUNK_SIZE,
        chunk_overlap=config.CHUNK_OVERLAP,
        separators=["\n\n", "\n", ". ", " ", ""],
    )
    chunks = splitter.split_documents(pages)
    return chunks


def get_embedding_model():
    """Load the local, free HuggingFace sentence-transformers model."""
    embeddings = HuggingFaceEmbeddings(model_name=config.EMBEDDING_MODEL_NAME)
    return embeddings


def reset_vector_store():
    """
    Wipe any previously stored collection.

    This keeps the demo simple: every time a new PDF is uploaded we start
    a fresh collection instead of mixing vectors from different documents.
    """
    shutil.rmtree(config.CHROMA_DIR, ignore_errors=True)
    import os
    os.makedirs(config.CHROMA_DIR, exist_ok=True)


def build_vectorstore(chunks, embeddings):
    """Embed every chunk and persist the vectors into ChromaDB."""
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name=config.COLLECTION_NAME,
        persist_directory=config.CHROMA_DIR,
    )
    return vectorstore


def ingest_pdf(pdf_path: str):
    """
    Full ingestion pipeline for a single PDF file.

    Returns
    -------
    vectorstore : Chroma
        The vector store ready to be queried.
    stats : dict
        num_pages, num_chunks, embedding_dim, num_vectors
    """
    reset_vector_store()

    pages = load_pdf(pdf_path)
    chunks = split_documents(pages)
    embeddings = get_embedding_model()

    # Probe the embedding dimension with a tiny throwaway query
    embedding_dim = len(embeddings.embed_query("dimension probe"))

    vectorstore = build_vectorstore(chunks, embeddings)

    try:
        num_vectors = vectorstore._collection.count()
    except Exception:
        num_vectors = len(chunks)

    stats = {
        "num_pages": len(pages),
        "num_chunks": len(chunks),
        "embedding_dim": embedding_dim,
        "num_vectors": num_vectors,
    }

    return vectorstore, stats
