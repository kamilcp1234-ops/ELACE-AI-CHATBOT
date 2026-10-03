import re
from rank_bm25 import BM25Okapi


def tokenize(text):
    """
    Convert text into clean lowercase tokens.
    Removes punctuation so words like:
    'location?' and 'location'
    become the same token.
    """
    return re.findall(r"\b\w+\b", text.lower())


def create_bm25_index(chunks):

    tokenized_documents = [
        tokenize(chunk["text"])
        for chunk in chunks
    ]

    bm25 = BM25Okapi(tokenized_documents)

    return bm25


def search_bm25(query, chunks, bm25, top_k=5):

    tokenized_query = tokenize(query)

    scores = bm25.get_scores(tokenized_query)

    top_indices = scores.argsort()[-top_k:][::-1]

    results = []

    for index in top_indices:

        results.append({
            "filename": chunks[index]["filename"],
            "chunk_id": chunks[index]["chunk_id"],
            "text": chunks[index]["text"],
            "score": float(scores[index])
        })

    return results