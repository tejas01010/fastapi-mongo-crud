from ollama import embeddings
import chromadb

# ---------------------------
# Vector DB setup
# ---------------------------
import os
import chromadb

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
VECTOR_DB_PATH = os.path.join(BASE_DIR, "vector_db")

client = chromadb.PersistentClient(path=VECTOR_DB_PATH)

collection = client.get_or_create_collection(
    name="hr_policy_vectors"
)

collection = client.get_or_create_collection(
    name="hr_policy_vectors1"
)

THRESHOLD = 300


# ---------------------------
# Chunking logic
# ---------------------------
def chunk_text(text: str, chunk_size=100, overlap=40):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks


# ---------------------------
# NEW: Document ingestion
# ---------------------------
def create_vectors_from_document(text: str):
    chunks = chunk_text(text)
    
    print("\n[DEBUG] Total chunks created:", len(chunks))
    print("[DEBUG] Sample chunk:\n", chunks[0][:700])

    for chunk in chunks:
        response = embeddings(
            model="nomic-embed-text",
            prompt=chunk
        )

        vector = response["embedding"]

        collection.add(
            documents=[chunk],
            embeddings=[vector],
            ids=[str(collection.count() + 1)]
        )

    return {
        "message": "Document processed successfully",
        "chunks_stored": len(chunks)
    }


# ---------------------------
# Existing: Search logic
# ---------------------------
def search_vectors(query: str, top_k: int):
    response = embeddings(
        model="nomic-embed-text",
        prompt=query
    )

    query_vector = response["embedding"]

    results = collection.query(
        query_embeddings=[query_vector],
        n_results=top_k
    )

    documents = results["documents"][0]
    distances = results["distances"][0]

    filtered_results = []

    for doc, dist in zip(documents, distances):
        if dist <= THRESHOLD:
            filtered_results.append(
                {"document": doc, "distance": round(dist, 2)}
            )

    return filtered_results
