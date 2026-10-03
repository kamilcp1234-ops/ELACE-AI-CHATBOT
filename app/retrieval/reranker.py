from sentence_transformers import CrossEncoder


# Load the reranker model
model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")


def rerank(query, results, top_k=3):
    pairs = []

    # Create question + document pairs
    for result in results:
        pairs.append((query, result["text"]))

    # Calculate relevance scores
    scores = model.predict(pairs)

    # Add the score to each result
    for result, score in zip(results, scores):
        result["rerank_score"] = float(score)

    # Sort by reranker score
    ranked_results = sorted(
        results,
        key=lambda x: x["rerank_score"],
        reverse=True
    )

    # Return the best results
    return ranked_results[:top_k]