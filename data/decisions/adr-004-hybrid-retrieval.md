# ADR-004: Adopt Hybrid Graph and Vector Retrieval

Decision ID: ADR-004

Date: August 29, 2026

Project Phoenix experienced a retrieval quality issue when vector search alone returned semantically relevant but incomplete context.

The AI Platform Team decided to combine vector similarity search with knowledge graph traversal.

Vector search retrieves relevant document chunks.

Graph retrieval follows relationships between entities.

The combined approach is called hybrid GraphRAG retrieval.

Neo4j is used for graph storage and retrieval.

This decision supersedes the earlier vector-only retrieval approach for Project Phoenix.