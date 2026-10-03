def hybrid_search(query, chunks, vector_results, bm25_results, top_k=5):

    combined = {}

    # -----------------------------
    # Vector Search Results
    # -----------------------------
    for rank, result in enumerate(vector_results, start=1):

        key = (
            result["filename"],
            result["chunk_id"]
        )

        combined[key] = {
            "filename": result["filename"],
            "chunk_id": result["chunk_id"],
            "text": result["text"],
            "score": 1 / (60 + rank)
        }

    # -----------------------------
    # BM25 Search Results
    # -----------------------------
    for rank, result in enumerate(bm25_results, start=1):

        key = (
            result["filename"],
            result["chunk_id"]
        )

        if key in combined:

            # Add BM25 RRF score
            combined[key]["score"] += 1 / (60 + rank)

        else:

            combined[key] = {
                "filename": result["filename"],
                "chunk_id": result["chunk_id"],
                "text": result["text"],
                "score": 1 / (60 + rank)
            }

    # -----------------------------
    # Sort by RRF Score
    # -----------------------------
    ranked_results = sorted(
        combined.values(),
        key=lambda x: x["score"],
        reverse=True
    )

    # -----------------------------
    # Return Top Results
    # -----------------------------
    return ranked_results[:top_k]