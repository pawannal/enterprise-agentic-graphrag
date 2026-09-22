# ADR-003: Standardize MCP Tool Permissions

Decision ID: ADR-003

Date: July 25, 2026

NexaAI decided that MCP tools must use explicit authentication and authorization.

AI agents must not invoke unapproved MCP tools.

Every production MCP tool must have an owner, permission requirements, and audit logging.

The Security Engineering Team owns the security requirements.

Project Phoenix and Project Orion must follow this decision.

The decision was introduced to reduce unauthorized tool access.