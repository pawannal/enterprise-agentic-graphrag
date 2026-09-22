import os

from dotenv import load_dotenv
from neo4j import GraphDatabase


load_dotenv()

URI = os.getenv("NEO4J_URI")
USERNAME = os.getenv("NEO4J_USERNAME")
PASSWORD = os.getenv("NEO4J_PASSWORD")
DATABASE = os.getenv("NEO4J_DATABASE", "neo4j")


driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)

try:
    driver.verify_connectivity()
    print("✅ Successfully connected to Neo4j Aura")

    result = driver.execute_query(
        "RETURN 'Hello from Python + Neo4j!' AS message",
        database_=DATABASE
    )

    print(result.records[0]["message"])

finally:
    driver.close()