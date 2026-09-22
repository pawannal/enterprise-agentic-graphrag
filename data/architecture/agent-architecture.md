# Agent Architecture

Project Orion uses a multi-step AI agent architecture.

Agents can reason about user requests, select appropriate tools, retrieve information, and produce responses.

LangGraph is used to orchestrate agent workflows.

MCP is used to connect agents with approved external tools.

Project Phoenix also uses agent workflows for GraphRAG retrieval.

Agent workflows must follow NexaAI security and tool permission policies.

The AI Platform Team defines reusable agent orchestration patterns.