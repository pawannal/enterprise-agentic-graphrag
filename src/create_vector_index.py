import os

from dotenv import load_dotenv
from neo4j import GraphDatabase
from neo4j_graphrag.indexes import create_vector_index


load_dotenv()

URI = os.getenv("NEO4J_URI")
USERNAME = os.getenv("NEO4J_USERNAME")
PASSWORD = os.getenv("NEO4J_PASSWORD")
DATABASE = os.getenv("NEO4J_DATABASE")

INDEX_NAME = "chunk_vector_index"


driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)


def main():
    driver.verify_connectivity()

    create_vector_index(
        driver,
        INDEX_NAME,
        label="Chunk",
        embedding_property="embedding",
        dimensions=1536,
        similarity_fn="cosine",
    )

    print(f"✅ Vector index '{INDEX_NAME}' created successfully")


if __name__ == "__main__":
    try:
        main()
    finally:
        driver.close()