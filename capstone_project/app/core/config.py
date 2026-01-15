import os
from dotenv import load_dotenv

load_dotenv()

# -----------------------------
# API / MODELS
# -----------------------------
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
LLM_MODEL = os.getenv("LLM_MODEL", "llama-3.1-8b-instant")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")

# -----------------------------
# PATHS
# -----------------------------
TEXT_CORPUS_DIR = os.getenv("TEXT_CORPUS_DIR", "data/corpus")
PDF_CORPUS_DIR = os.getenv("PDF_CORPUS_DIR", "data/pdfs")
VECTOR_STORE_DIR = os.getenv("VECTOR_STORE_DIR", "vector_store")

VECTOR_STORE_PATH = os.path.join(VECTOR_STORE_DIR, "faiss.index")
META_PATH = os.path.join(VECTOR_STORE_DIR, "metadata.pkl")

# -----------------------------
# CHUNKING
# -----------------------------
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

# -----------------------------
# API URL (for Streamlit)
# -----------------------------
BACKEND_API_URL = os.getenv(
    "BACKEND_API_URL",
    "http://127.0.0.1:8000/tutor/ask"
)
