import os
from dotenv import load_dotenv
from neo4j import GraphDatabase

from neo4j_graphrag.embeddings.openai import OpenAIEmbeddings
from neo4j_graphrag.retrievers import VectorCypherRetriever

load_dotenv()

URI = os.getenv("NEO4J_URI")
USERNAME = os.getenv("NEO4J_USERNAME")
PASSWORD = os.getenv("NEO4J_PASSWORD")
DATABASE = os.getenv("NEO4J_DATABASE")

INDEX_NAME = "chunk_vector_index"


def main():

    driver = GraphDatabase.driver(
        URI,
        auth=(USERNAME, PASSWORD)
    )

    driver.verify_connectivity()

    print("✅ Connected to Neo4j")

    embedder = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

    retrieval_query = """
    OPTIONAL MATCH (project:Project)-[:FROM_CHUNK]->(node)
    OPTIONAL MATCH (project)-[:USES]->(technology:Technology)

    RETURN
        node.text AS chunk_text,
        node.source AS source,
        project.name AS project,
        collect(technology.name) AS technologies,
        score
    """

    retriever = VectorCypherRetriever(
        driver=driver,
        index_name=INDEX_NAME,
        retrieval_query=retrieval_query,
        embedder=embedder,
        neo4j_database=DATABASE,
    )

    query = "Which projects use Python?"

    print(f"\n🔎 Query: {query}")

    result = retriever.search(
        query_text=query,
        top_k=5
    )

    print("\n========== GRAPHRAG RETRIEVAL RESULTS ==========")

    for item in result.items:
        print("CONTENT:", item.content)
        print("METADATA:", item.metadata)
        print("-" * 60)

    driver.close()


if __name__ == "__main__":
    main()