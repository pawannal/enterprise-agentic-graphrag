import asyncio
from pathlib import Path

from neo4j_graphrag.components.text_splitters.fixed_size_splitter import (
    FixedSizeSplitter,
)


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


async def main():
    documents = load_markdown_files()

    splitter = FixedSizeSplitter(
        chunk_size=500,
        chunk_overlap=100,
        approximate=True,
    )

    total_chunks = 0

    for document in documents:
        result = await splitter.run(document["text"])

        chunks = result.chunks

        total_chunks += len(chunks)

        print(f"\nDocument: {document['path']}")
        print(f"Chunks: {len(chunks)}")

        for chunk in chunks[:2]:
            print(f"\n--- Chunk {chunk.index} ---")
            print(chunk.text[:300])

    print("\n==============================")
    print(f"Documents: {len(documents)}")
    print(f"Total chunks: {total_chunks}")
    print("==============================")


if __name__ == "__main__":
    asyncio.run(main())