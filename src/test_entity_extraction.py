import asyncio

from neo4j_graphrag.components.entity_relation_extractor import (
    LLMEntityRelationExtractor,
)
from neo4j_graphrag.components.types import TextChunks, TextChunk
from neo4j_graphrag.llm import OpenAILLM

from graph_schema import build_graph_schema
from dotenv import load_dotenv

load_dotenv()

async def main():

    # 1. Build our graph schema
    schema = build_graph_schema()

    # 2. Create the LLM
    llm = OpenAILLM(
        model_name="gpt-4.1-mini",
        model_params={
            "temperature": 0
        },
    )

    # 3. Create the entity/relation extractor
    extractor = LLMEntityRelationExtractor(
        llm=llm,
        use_structured_output=True,
    )

    # 4. One test chunk
    text = """
    Project Atlas uses Python for data ingestion and transformation.
    """

    chunks = TextChunks(
        chunks=[
            TextChunk(
                text=text,
                index=0,
            )
        ]
    )

    # 5. Extract entities and relationships
    result = await extractor.run(
        chunks=chunks,
        schema=schema,
    )

    print("\n========== EXTRACTION RESULT ==========")

    print(result)

    print("\n=======================================")


if __name__ == "__main__":
    asyncio.run(main())