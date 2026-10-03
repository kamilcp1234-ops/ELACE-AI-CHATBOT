
from pathlib import Path


DOCUMENTS_DIR = Path("documents")


def load_documents():
    documents = []

    # Search all folders and subfolders
    for file_path in DOCUMENTS_DIR.rglob("*.md"):

        text = file_path.read_text(encoding="utf-8")

        # Store the relative path as the source
        relative_path = file_path.relative_to(DOCUMENTS_DIR)

        documents.append({
            "filename": str(relative_path),
            "text": text
        })

    return documents

