# Retrieval Architecture

Project Phoenix uses hybrid retrieval to improve enterprise question answering.

Vector retrieval identifies semantically relevant document chunks.

Graph retrieval follows relationships between entities such as projects, people, technologies, teams, customers, incidents, and policies.

The retrieval layer can combine vector results and graph results before passing context to the language model.

Neo4j is used for graph storage and graph retrieval.

OpenAI models are used to generate embeddings and responses where configured.

The retrieval architecture is maintained by the AI Platform Team.