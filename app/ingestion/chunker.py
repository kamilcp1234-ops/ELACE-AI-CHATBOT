def chunk_documents(documents, chunk_size=800, overlap=150):
    chunks = []

    for document in documents:
        text = document["text"]
        filename = document["filename"]

        start = 0
        chunk_id = 0

        while start < len(text):

            end = start + chunk_size

            chunk_text = text[start:end].strip()

            if chunk_text:
                chunks.append({
                    "filename": filename,
                    "chunk_id": chunk_id,
                    "text": chunk_text
                })

                chunk_id += 1

            # Move forward while keeping overlap
            start = end - overlap

    return chunks