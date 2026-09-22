import asyncio
import os

from dotenv import load_dotenv
from neo4j import GraphDatabase

from neo4j_graphrag.components.resolver import (
    SinglePropertyExactMatchResolver,
)


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

    resolver = SinglePropertyExactMatchResolver(
        driver=driver,
        resolve_property="name",
        neo4j_database=DATABASE,
    )

    print("🔗 Resolving duplicate entities...")

    result = await resolver.run()

    print("\n========== ENTITY RESOLUTION ==========")
    print(f"Entities processed: {result.number_of_nodes_to_resolve}")
    print(f"Entities created after merge: {result.number_of_created_nodes}")

    driver.close()


if __name__ == "__main__":
    asyncio.run(main())