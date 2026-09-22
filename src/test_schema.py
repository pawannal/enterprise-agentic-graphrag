from graph_schema import build_graph_schema


def main():
    schema = build_graph_schema()

    print("✅ Graph schema created successfully")
    print(f"Node types: {len(schema.node_types)}")
    print(f"Relationship types: {len(schema.relationship_types)}")
    print(f"Patterns: {len(schema.patterns)}")

    print("\nNodes:")
    for node in schema.node_types:
        print(f"- {node.label}")

    print("\nRelationships:")
    for relationship in schema.relationship_types:
        print(f"- {relationship.label}")


if __name__ == "__main__":
    main()