from app.ingestion.document_loader import load_documents
from app.ingestion.chunker import chunk_documents

from app.retrieval.vector_search import create_embeddings, search
from app.retrieval.bm25_search import create_bm25_index, search_bm25
from app.retrieval.hybrid_search import hybrid_search
from app.retrieval.reranker import rerank

from app.generation.llm import generate_answer


# ============================================================
# LOAD DOCUMENTS
# ============================================================

documents = load_documents()

print("\n===== DOCUMENT LOADING =====")
print("Documents loaded:", len(documents))

for document in documents:
    print(document["filename"])


# ============================================================
# CHUNK DOCUMENTS
# ============================================================

chunks = chunk_documents(documents)

print("\n===== CHUNKING =====")
print("Total documents:", len(documents))
print("Total chunks:", len(chunks))


# ============================================================
# CREATE SEARCH INDEXES
# ============================================================

embeddings = create_embeddings(chunks)

bm25 = create_bm25_index(chunks)


# ============================================================
# ASK QUESTION
# ============================================================

def ask_question(query):

    query = query.strip()

    if not query:
        return "Please enter a question."


    # ========================================================
    # STEP 1: VECTOR SEARCH
    # ========================================================

    vector_results = search(
        query,
        chunks,
        embeddings,
        top_k=10
    )


    # ========================================================
    # STEP 2: BM25 SEARCH
    # ========================================================

    bm25_results = search_bm25(
        query,
        chunks,
        bm25,
        top_k=10
    )


    # ========================================================
    # STEP 3: HYBRID SEARCH
    # ========================================================

    hybrid_results = hybrid_search(
        query,
        chunks,
        vector_results,
        bm25_results,
        top_k=10
    )


    print("\n===== HYBRID RESULTS =====")

    for result in hybrid_results:

        print("\nFilename:", result["filename"])
        print("Score:", result["score"])
        print("Text:", result["text"])


    # ========================================================
    # STEP 4: RERANK
    # ========================================================

    reranked_results = rerank(
        query,
        hybrid_results,
        top_k=5
    )


    print("\n===== RERANKED RESULTS =====")

    for result in reranked_results:

        print("\nFilename:", result["filename"])
        print("Rerank Score:", result["rerank_score"])
        print("Text:", result["text"])


    # ========================================================
    # STEP 5: CREATE FINAL CONTEXT
    # ========================================================

    context = "\n\n".join(
        result["text"]
        for result in reranked_results
    )


    print("\n===== FINAL CONTEXT =====")
    print(context)


    # ========================================================
    # STEP 6: GENERATE ANSWER
    # ========================================================

    answer = generate_answer(
        query,
        context
    )


    return answer