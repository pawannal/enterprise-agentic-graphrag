import os

from dotenv import load_dotenv
from neo4j import GraphDatabase


load_dotenv()

URI = os.getenv("NEO4J_URI")
USERNAME = os.getenv("NEO4J_USERNAME")
PASSWORD = os.getenv("NEO4J_PASSWORD")
DATABASE = os.getenv("NEO4J_DATABASE")

driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)


def main():
    driver.verify_connectivity()

    records, summary, keys = driver.execute_query(
        """
        MATCH (n)
        RETURN labels(n) AS labels, count(n) AS count
        ORDER BY count DESC
        """,
        database_=DATABASE,
    )

    print("\n=== Nodes by Label ===")

    for record in records:
        print(record["labels"], "->", record["count"])

    records, summary, keys = driver.execute_query(
        """
        MATCH ()-[r]->()
        RETURN type(r) AS relationship, count(r) AS count
        ORDER BY count DESC
        """,
        database_=DATABASE,
    )

    print("\n=== Relationships ===")

    for record in records:
        print(record["relationship"], "->", record["count"])


if __name__ == "__main__":
    try:
        main()
    finally:
        driver.close()