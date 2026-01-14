import os
import faiss
import pickle
from sentence_transformers import SentenceTransformer


CORPUS_DIR = "data/corpus"
VECTOR_STORE_PATH = "vector_store/faiss.index"
META_PATH = "vector_store/metadata.pkl"

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


def load_documents():
    documents = []
    for filename in os.listdir(CORPUS_DIR):
        if filename.endswith(".txt"):
            with open(os.path.join(CORPUS_DIR, filename), "r", encoding="utf-8") as f:
                documents.append(f.read())
    return documents


def build_vector_store():
    documents = load_documents()
    embeddings = embedding_model.encode(documents)

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    os.makedirs("vector_store", exist_ok=True)
    faiss.write_index(index, VECTOR_STORE_PATH)

    with open(META_PATH, "wb") as f:
        pickle.dump(documents, f)


def retrieve_context(query: str, k: int = 2):
    index = faiss.read_index(VECTOR_STORE_PATH)

    with open(META_PATH, "rb") as f:
        documents = pickle.load(f)

    query_embedding = embedding_model.encode([query])
    distances, indices = index.search(query_embedding, k)

    results = [documents[i] for i in indices[0]]
    avg_distance = float(distances[0].mean())

    return "\n".join(results), avg_distance
