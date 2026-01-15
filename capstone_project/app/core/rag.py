import os
import faiss
import pickle
from typing import List, Tuple
from sentence_transformers import SentenceTransformer
from PyPDF2 import PdfReader

from app.core.config import (
    TEXT_CORPUS_DIR,
    PDF_CORPUS_DIR,
    VECTOR_STORE_DIR,
    VECTOR_STORE_PATH,
    META_PATH,
    EMBEDDING_MODEL,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)

# -----------------------------
# EMBEDDING MODEL
# -----------------------------
embedding_model = SentenceTransformer(EMBEDDING_MODEL)



# -----------------------------
# TEXT EXTRACTION
# -----------------------------
def load_txt_files() -> List[str]:
    texts = []
    for filename in os.listdir(TEXT_CORPUS_DIR):
        if filename.endswith(".txt"):
            with open(os.path.join(TEXT_CORPUS_DIR, filename), "r", encoding="utf-8") as f:
                texts.append(f.read())
    return texts


def load_pdf_files() -> List[str]:
    texts = []
    for filename in os.listdir(PDF_CORPUS_DIR):
        if filename.endswith(".pdf"):
            reader = PdfReader(os.path.join(PDF_CORPUS_DIR, filename))
            pdf_text = ""
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    pdf_text += page_text + "\n"
            texts.append(pdf_text)
    return texts


# -----------------------------
# CHUNKING
# -----------------------------
def chunk_text(text: str) -> List[str]:
    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + CHUNK_SIZE
        chunk = text[start:end]
        chunks.append(chunk)
        start += CHUNK_SIZE - CHUNK_OVERLAP

    return chunks


# -----------------------------
# BUILD VECTOR STORE
# -----------------------------
def build_vector_store():
    all_texts = []

    txt_texts = load_txt_files()
    pdf_texts = load_pdf_files()

    for text in txt_texts + pdf_texts:
        chunks = chunk_text(text)
        all_texts.extend(chunks)

    embeddings = embedding_model.encode(all_texts, show_progress_bar=True)

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    os.makedirs(VECTOR_STORE_DIR, exist_ok=True)
    faiss.write_index(index, VECTOR_STORE_PATH)

    with open(META_PATH, "wb") as f:
        pickle.dump(all_texts, f)

    print(f"✅ FAISS index built with {len(all_texts)} chunks")


# -----------------------------
# RETRIEVAL
# -----------------------------
def retrieve_context(query: str, k: int = 4) -> Tuple[str, float]:
    index = faiss.read_index(VECTOR_STORE_PATH)

    with open(META_PATH, "rb") as f:
        chunks = pickle.load(f)

    query_embedding = embedding_model.encode([query])
    distances, indices = index.search(query_embedding, k)

    retrieved_chunks = [chunks[i] for i in indices[0]]
    avg_distance = float(distances[0].mean())

    return "\n\n".join(retrieved_chunks), avg_distance

# this function created just for testing purpose
def load_documents() -> List[str]:
    return load_txt_files() + load_pdf_files()
