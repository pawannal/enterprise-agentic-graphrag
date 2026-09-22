import asyncio
import os

from dotenv import load_dotenv
from neo4j import GraphDatabase

from neo4j_graphrag.components.neo4j_reader import Neo4jChunkReader
from neo4j_graphrag.components.entity_relation_extractor import (
    LLMEntityRelationExtractor,
)
from neo4j_graphrag.components.kg_writer import Neo4jWriter
from neo4j_graphrag.llm import OpenAILLM

from graph_schema import build_graph_schema


load_dotenv()

URI = os.getenv("NEO4J_URI")
USERNAME = os.getenv("NEO4J_USERNAME")
PASSWORD = os.getenv("NEO4J_PASSWORD")
DATABASE = os.getenv("NEO4J_DATABASE")


async def main():

    driver = GraphDatabase.driver(
        URI,
        auth=(USERNAME, PASSWORD)
    )

    driver.verify_connectivity()

    print("✅ Connected to Neo4j")

    # --------------------------------------------------
    # 1. Read existing chunks
    # --------------------------------------------------

    reader = Neo4jChunkReader(
        driver=driver,
        fetch_embeddings=True,
        neo4j_database=DATABASE,
    )

    chunks = await reader.run()

    print(f"📄 Chunks loaded: {len(chunks.chunks)}")

    # --------------------------------------------------
    # 2. Create LLM
    # --------------------------------------------------

    llm = OpenAILLM(
        model_name="gpt-4.1-mini",
        model_params={
            "temperature": 0
        },
    )

    # --------------------------------------------------
    # 3. Extract entities and relationships
    # --------------------------------------------------

    extractor = LLMEntityRelationExtractor(
        llm=llm,
        use_structured_output=True,
        create_lexical_graph=True,
        max_concurrency=5,
    )

    schema = build_graph_schema()

    print("🧠 Extracting entities and relationships...")

    graph = await extractor.run(
        chunks=chunks,
        schema=schema,
    )

    print(f"Nodes extracted: {len(graph.nodes)}")
    print(f"Relationships extracted: {len(graph.relationships)}")

    # --------------------------------------------------
    # 4. Write graph to Neo4j
    # --------------------------------------------------

    writer = Neo4jWriter(
        driver=driver,
        neo4j_database=DATABASE,
        batch_size=1000,
        clean_db=False,
    )

    print("💾 Writing knowledge graph to Neo4j...")

    result = await writer.run(graph)

    print("\n========== KG BUILD RESULT ==========")
    print(result)

    driver.close()


if __name__ == "__main__":
    asyncio.run(main())