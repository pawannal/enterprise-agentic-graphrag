from dotenv import load_dotenv
from neo4j_graphrag.embeddings.openai import OpenAIEmbeddings


load_dotenv()


def main():
    embedder = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

    text = """
    Project Atlas uses Python for data ingestion and transformation.
    """

    embedding = embedder.embed_query(text)

    print("Embedding generated successfully!")
    print("Vector dimensions:", len(embedding))
    print("First 10 values:", embedding[:10])


if __name__ == "__main__":
    main()