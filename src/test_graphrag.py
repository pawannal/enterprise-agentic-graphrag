import os

from dotenv import load_dotenv
from neo4j import GraphDatabase

from neo4j_graphrag.embeddings.openai import OpenAIEmbeddings
from neo4j_graphrag.retrievers import VectorCypherRetriever
from neo4j_graphrag.llm import OpenAILLM
from neo4j_graphrag.generation import GraphRAG


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

    # --------------------------------------------------
    # 1. Embedding model
    # --------------------------------------------------

    embedder = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

    # --------------------------------------------------
    # 2. Graph-aware retrieval query
    # --------------------------------------------------

    retrieval_query = """
    OPTIONAL MATCH (project:Project)-[:FROM_CHUNK]->(node)
    OPTIONAL MATCH (project)-[:USES]->(technology:Technology)

    RETURN
        node.text AS chunk_text,
        node.source AS source,
        project.name AS project,
        collect(DISTINCT technology.name) AS technologies,
        score
    """

    # --------------------------------------------------
    # 3. GraphRAG retriever
    # --------------------------------------------------

    retriever = VectorCypherRetriever(
        driver=driver,
        index_name=INDEX_NAME,
        retrieval_query=retrieval_query,
        embedder=embedder,
        neo4j_database=DATABASE,
    )

    # --------------------------------------------------
    # 4. LLM
    # --------------------------------------------------

    llm = OpenAILLM(
        model_name="gpt-4.1-mini",
        model_params={
            "temperature": 0
        },
    )

    # --------------------------------------------------
    # 5. GraphRAG pipeline
    # --------------------------------------------------

    rag = GraphRAG(
        retriever=retriever,
        llm=llm,
    )

    query = "Which projects use Python and what do they use it for?"

    print(f"\n🔎 Question: {query}")

    response = rag.search(
        query_text=query,
        retriever_config={
            "top_k": 5
        },
    )

    print("\n========== FINAL ANSWER ==========")
    print(response.answer)

    driver.close()


if __name__ == "__main__":
    main()