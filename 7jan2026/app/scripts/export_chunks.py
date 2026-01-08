import os
import csv
import chromadb

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
VECTOR_DB_PATH = os.path.join(BASE_DIR, "vector_db")

client = chromadb.PersistentClient(path=VECTOR_DB_PATH)

print("\n[DEBUG] Available collections:")
for col in client.list_collections():
    print("-", col.name)

collection = client.get_collection(name="hr_policy_vectors1")

data = collection.get()

documents = data["documents"]
ids = data["ids"]

ARTIFACTS_DIR = os.path.join(BASE_DIR, "artifacts")
os.makedirs(ARTIFACTS_DIR, exist_ok=True)

output_file = os.path.join(ARTIFACTS_DIR, "hr_policy_chunks.csv")

with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["chunk_id", "chunk_text"])

    for cid, doc in zip(ids, documents):
        writer.writerow([cid, doc])

print(f"\n✅ Exported {len(documents)} chunks to {output_file}")
