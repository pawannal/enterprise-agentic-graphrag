# ADR-001: Adopt GraphRAG for Enterprise Retrieval

Decision ID: ADR-001

Date: June 15, 2026

Project Phoenix initially used standard vector-based RAG.

The team observed that vector retrieval was not sufficient for questions requiring relationships between people, projects, technologies, policies, and incidents.

The AI Platform Team decided to adopt a GraphRAG architecture.

Neo4j was selected as the knowledge graph database.

The architecture combines vector retrieval with graph retrieval.

This decision applies to Project Phoenix.

The decision was approved by the AI Platform Team.