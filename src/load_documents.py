from pathlib import Path


DATA_DIR = Path("data")


def load_markdown_files():
    documents = []

    for file_path in DATA_DIR.rglob("*.md"):
        text = file_path.read_text(encoding="utf-8")

        documents.append(
            {
                "path": str(file_path),
                "text": text,
            }
        )

    return documents


if __name__ == "__main__":
    documents = load_markdown_files()

    print(f"Found {len(documents)} Markdown documents")

    for document in documents:
        print(f"- {document['path']}")