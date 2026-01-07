from ollama import embeddings
import chromadb

client = chromadb.PersistentClient(path="./vector_db")

collection = client.get_or_create_collection(
    name="policy_vectors"
)

THRESHOLD = 300


def create_vector(text: str):
    response = embeddings(
        model="nomic-embed-text",
        prompt=text
    )

    vector = response["embedding"]

    collection.add(
        documents=[text],
        embeddings=[vector],
        ids=[str(collection.count() + 1)]
    )

    return {"message": "Vector created successfully"}


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
                {"document": doc, "distance": dist}
            )

    return filtered_results
