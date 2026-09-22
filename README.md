# Enterprise Agentic GraphRAG

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Neo4j](https://img.shields.io/badge/Neo4j-GraphRAG-blue?logo=neo4j)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4.1--mini-black?logo=openai)
![GraphRAG](https://img.shields.io/badge/Architecture-GraphRAG-purple)

An enterprise-focused **Graph Retrieval-Augmented Generation (GraphRAG)** system built with **Python, Neo4j, OpenAI, and the Neo4j GraphRAG Python package**.

The system combines **semantic vector retrieval** with **knowledge graph traversal** to retrieve relationship-aware context before generating answers with an LLM.

---

## Table of Contents

- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Why GraphRAG](#why-graphrag)
- [Architecture](#architecture)
- [End-to-End Flow](#end-to-end-flow)
- [Knowledge Graph](#knowledge-graph)
- [Data Ingestion Pipeline](#data-ingestion-pipeline)
- [Knowledge Graph Construction](#knowledge-graph-construction)
- [Entity Resolution](#entity-resolution)
- [Retrieval Pipeline](#retrieval-pipeline)
- [Answer Generation](#answer-generation)
- [Example Query](#example-query)
- [Project Results](#project-results)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Environment Variables](#environment-variables)
- [Running the Pipeline](#running-the-pipeline)
- [Security](#security)
- [Troubleshooting](#troubleshooting)
- [Design Decisions](#design-decisions)
- [Limitations](#limitations)
- [Future Enhancements](#future-enhancements)
- [Key Concepts Demonstrated](#key-concepts-demonstrated)

---

# Overview

Enterprise knowledge is rarely stored as isolated pieces of information.

A typical enterprise environment contains:

- Projects
- Technologies
- Teams
- Employees
- Customers
- Policies
- Skills
- Incidents
- Decisions
- Relationships between these entities

Traditional vector RAG is effective at finding semantically similar text. However, questions involving multiple entities and their relationships can benefit from structured graph context in addition to semantic similarity.

This project addresses that requirement by combining:

1. **Document ingestion and chunking**
2. **Vector embeddings**
3. **Knowledge graph construction**
4. **Entity and relationship extraction**
5. **Entity resolution**
6. **Vector + graph retrieval**
7. **LLM-based answer generation**

The result is an end-to-end **Graph Retrieval-Augmented Generation (GraphRAG)** pipeline.

---

# Problem Statement

Consider the question:

> Which projects use Python and what do they use it for?

A vector retrieval system can identify chunks that are semantically related to Python.

However, the enterprise knowledge graph can explicitly represent relationships such as:

```text
Project Atlas
    |
    | USES
    ↓
  Python

Project Phoenix
    |
    | USES
    ↓
  Python

Project Orion
    |
    | USES
    ↓
  Python

# Architecture

![Enterprise GraphRAG System Architecture](docs/architecture/graphrag-system-architecture.png)

The system is organized into three major stages:

1. Data ingestion and knowledge graph construction
2. Vector + graph retrieval
3. LLM-based answer generation

Project Sentinel
    |
    | USES
    ↓
  Python
