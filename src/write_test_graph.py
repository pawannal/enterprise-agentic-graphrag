import asyncio
import os

from dotenv import load_dotenv
from neo4j import GraphDatabase

from neo4j_graphrag.components.entity_relation_extractor import (
    LLMEntityRelationExtractor,
)
from neo4j_graphrag.components.kg_writer import Neo4jWriter
from neo4j_graphrag.components.types import TextChunks, TextChunk
from neo4j_graphrag.llm import OpenAILLM

from graph_schema import build_graph_schema


load_dotenv()


URI = os.getenv("NEO4J_URI")
USERNAME = os.getenv("NEO4J_USERNAME")
PASSWORD = os.getenv("NEO4J_PASSWORD")
DATABASE = os.getenv("NEO4J_DATABASE")


async def main():

    # -----------------------------------
    # 1. Neo4j connection
    # -----------------------------------

    driver = GraphDatabase.driver(
        URI,
        auth=(USERNAME, PASSWORD),
    )

    driver.verify_connectivity()

    # -----------------------------------
    # 2. Graph schema
    # -----------------------------------

    schema = build_graph_schema()

    # -----------------------------------
    # 3. LLM
    # -----------------------------------

    llm = OpenAILLM(
        model_name="gpt-4.1-mini",
        model_params={
            "temperature": 0
        },
    )

    # -----------------------------------
    # 4. Entity / Relationship extractor
    # -----------------------------------

    extractor = LLMEntityRelationExtractor(
        llm=llm,
        use_structured_output=True,
    )

    # -----------------------------------
    # 5. One test chunk
    # -----------------------------------

    chunks = TextChunks(
        chunks=[
            TextChunk(
                text=(
                    "Project Atlas uses Python "
                    "for data ingestion and transformation."
                ),
                index=0,
                uid="test-atlas-001",
            )
        ]
    )

    # -----------------------------------
    # 6. Extract graph
    # -----------------------------------

    graph = await extractor.run(
        chunks=chunks,
        schema=schema,
    )

    print("\n========== EXTRACTED GRAPH ==========")

    print(f"Nodes: {len(graph.nodes)}")
    print(f"Relationships: {len(graph.relationships)}")

    for node in graph.nodes:
        print(
            f"NODE | {node.label} | "
            f"{node.properties}"
        )

    for relationship in graph.relationships:
        print(
            f"RELATIONSHIP | "
            f"{relationship.type} | "
            f"{relationship.start_node_id} -> "
            f"{relationship.end_node_id}"
        )

    # -----------------------------------
    # 7. Write graph to Neo4j
    # -----------------------------------

    writer = Neo4jWriter(
        driver=driver,
        neo4j_database=DATABASE,
        clean_db=False,
    )

    result = await writer.run(graph)

    print("\n========== WRITER RESULT ==========")
    print(result)

    driver.close()


if __name__ == "__main__":
    asyncio.run(main())