# GraphRAG Architecture

Project Phoenix uses a GraphRAG architecture to combine semantic retrieval with knowledge graph retrieval.

The architecture contains document ingestion, text chunking, embeddings, vector search, entity extraction, relationship extraction, and Neo4j graph retrieval.

Neo4j stores entities and relationships extracted from enterprise documents.

The retrieval layer can combine vector similarity results with graph traversal results before sending context to the language model.

Project Phoenix uses OpenAI models for language model capabilities and LangGraph for orchestration.

The AI Platform Team owns the GraphRAG architecture.