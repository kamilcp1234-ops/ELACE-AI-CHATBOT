import numpy as np
from sentence_transformers import SentenceTransformer


model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings(chunks):
    texts = [chunk["text"] for chunk in chunks]

    embeddings = model.encode(
        texts,
        normalize_embeddings=True
    )

    return embeddings


def search(query, chunks, embeddings, top_k=3):
    query_embedding = model.encode(
        [query],
        normalize_embeddings=True
    )[0]

    scores = np.dot(embeddings, query_embedding)

    top_indices = np.argsort(scores)[-top_k:][::-1]

    results = []

    for index in top_indices:
        results.append({
            "filename": chunks[index]["filename"],
            "chunk_id": chunks[index]["chunk_id"],
            "text": chunks[index]["text"],
            "score": float(scores[index])
        })

    return results