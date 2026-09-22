import asyncio
import os
from pathlib import Path

from dotenv import load_dotenv
from neo4j import GraphDatabase
from neo4j_graphrag.components.text_splitters.fixed_size_splitter import (
    FixedSizeSplitter,
)
from neo4j_graphrag.embeddings.openai import OpenAIEmbeddings


load_dotenv()


DATA_DIR = Path("data")
INDEX_NAME = "chunk_vector_index"


URI = os.getenv("NEO4J_URI")
USERNAME = os.getenv("NEO4J_USERNAME")
PASSWORD = os.getenv("NEO4J_PASSWORD")
DATABASE = os.getenv("NEO4J_DATABASE")


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
    driver = GraphDatabase.driver(
        URI,
        auth=(USERNAME, PASSWORD),
    )

    driver.verify_connectivity()

    splitter = FixedSizeSplitter(
        chunk_size=500,
        chunk_overlap=100,
        approximate=True,
    )

    embedder = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

    documents = load_markdown_files()

    total_chunks = 0

    for document in documents:

        result = await splitter.run(document["text"])
        chunks = result.chunks

        for chunk in chunks:

            embedding = embedder.embed_query(chunk.text)

            driver.execute_query(
                """
                CREATE (c:Chunk {
                    chunk_id: $chunk_id,
                    text: $text,
                    source: $source,
                    embedding: $embedding
                })
                """,
                chunk_id=f"{document['path']}::{chunk.index}",
                text=chunk.text,
                source=document["path"],
                embedding=embedding,
                database_=DATABASE,
            )

            total_chunks += 1

        print(
            f"Processed {document['path']} "
            f"({len(chunks)} chunks)"
        )

    driver.close()

    print("\n==============================")
    print(f"Documents: {len(documents)}")
    print(f"Chunks stored: {total_chunks}")
    print("==============================")


if __name__ == "__main__":
    asyncio.run(main())