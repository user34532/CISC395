import os
import chromadb
from sentence_transformers import SentenceTransformer
from pypdf import PdfReader

GUIDES_DIR = "guides"
DB_DIR = "chroma_db"

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path=DB_DIR)


def read_file(path):
    if path.endswith(".pdf"):
        reader = PdfReader(path)
        text = ""
        for p in reader.pages:
            t = p.extract_text()
            if t:
                text += t
        return text
    else:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()


def chunk_text(text, size=200):
    words = text.split()
    chunks = []
    for i in range(0, len(words), size):
        chunk = " ".join(words[i:i+size])
        if chunk.strip():
            chunks.append(chunk)
    return chunks


def build_index():
    try:
        client.delete_collection("guides")
    except:
        pass

    collection = client.create_collection(name="guides")

    count = 0

    for file in os.listdir(GUIDES_DIR):
        path = os.path.join(GUIDES_DIR, file)

        if not os.path.isfile(path):
            continue

        text = read_file(path)
        chunks = chunk_text(text)

        for i, chunk in enumerate(chunks):
            embedding = model.encode(chunk).tolist()

            collection.add(
                documents=[chunk],
                embeddings=[embedding],
                ids=[f"{file}_{i}_{count}"]
            )

            count += 1

    print(f"Indexed {count} chunks.")


def search_guides(query):
    collection = client.get_or_create_collection(name="guides")

    embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=3
    )

    if results and results["documents"]:
        return results["documents"][0]

    return []


if __name__ == "__main__":
    build_index()
