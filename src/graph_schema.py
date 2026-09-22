from neo4j_graphrag.components.schema import (
    GraphSchema,
    NodeType,
    PropertyType,
    RelationshipType,
    Pattern,
)


def build_graph_schema() -> GraphSchema:

    node_types = (
        NodeType(
            label="Person",
            description="An individual person involved in projects or teams.",
            properties=[
                PropertyType(
                    name="name",
                    type="STRING",
                    description="The person's name",
                )
            ],
        ),
        NodeType(
            label="Team",
            description="A group of people responsible for projects or capabilities.",
            properties=[
                PropertyType(
                    name="name",
                    type="STRING",
                    description="The team's name",
                )
            ],
        ),
        NodeType(
            label="Project",
            description="A software, AI, or business project.",
            properties=[
                PropertyType(
                    name="name",
                    type="STRING",
                    description="The project's name",
                )
            ],
        ),
        NodeType(
            label="Technology",
            description="A programming language, framework, platform, database, or tool.",
            properties=[
                PropertyType(
                    name="name",
                    type="STRING",
                    description="The technology name",
                )
            ],
        ),
        NodeType(
            label="Customer",
            description="A customer or organization served by a project.",
            properties=[
                PropertyType(
                    name="name",
                    type="STRING",
                    description="The customer's name",
                )
            ],
        ),
        NodeType(
            label="Skill",
            description="A technical or professional skill.",
            properties=[
                PropertyType(
                    name="name",
                    type="STRING",
                    description="The skill name",
                )
            ],
        ),
        NodeType(
            label="Policy",
            description="A policy, standard, or governance requirement.",
            properties=[
                PropertyType(
                    name="name",
                    type="STRING",
                    description="The policy name",
                )
            ],
        ),
        NodeType(
            label="Incident",
            description="A production, security, operational, or technical incident.",
            properties=[
                PropertyType(
                    name="name",
                    type="STRING",
                    description="The incident name",
                )
            ],
        ),
        NodeType(
            label="Decision",
            description="An architecture, technical, or business decision.",
            properties=[
                PropertyType(
                    name="name",
                    type="STRING",
                    description="The decision name",
                )
            ],
        ),
    )

    relationship_types = (
        RelationshipType(
            label="MEMBER_OF",
            description="Person is a member of a team.",
        ),
        RelationshipType(
            label="WORKS_ON",
            description="Person works on a project.",
        ),
        RelationshipType(
            label="HAS_SKILL",
            description="Person has a skill.",
        ),
        RelationshipType(
            label="OWNS",
            description="Team owns a project.",
        ),
        RelationshipType(
            label="USES",
            description="Project uses a technology.",
        ),
        RelationshipType(
            label="SERVES",
            description="Project serves a customer.",
        ),
        RelationshipType(
            label="GOVERNED_BY",
            description="Project is governed by a policy.",
        ),
        RelationshipType(
            label="AFFECTED_BY",
            description="Project is affected by an incident.",
        ),
        RelationshipType(
            label="ABOUT",
            description="Decision is about a project.",
        ),
        RelationshipType(
            label="AFFECTS",
            description="Incident affects a project.",
        ),
    )

    patterns = (
        Pattern(
            source="Person",
            relationship="MEMBER_OF",
            target="Team",
        ),
        Pattern(
            source="Person",
            relationship="WORKS_ON",
            target="Project",
        ),
        Pattern(
            source="Person",
            relationship="HAS_SKILL",
            target="Skill",
        ),
        Pattern(
            source="Team",
            relationship="OWNS",
            target="Project",
        ),
        Pattern(
            source="Project",
            relationship="USES",
            target="Technology",
        ),
        Pattern(
            source="Project",
            relationship="SERVES",
            target="Customer",
        ),
        Pattern(
            source="Project",
            relationship="GOVERNED_BY",
            target="Policy",
        ),
        Pattern(
            source="Project",
            relationship="AFFECTED_BY",
            target="Incident",
        ),
        Pattern(
            source="Decision",
            relationship="ABOUT",
            target="Project",
        ),
        Pattern(
            source="Incident",
            relationship="AFFECTS",
            target="Project",
        ),
    )

    return GraphSchema(
        node_types=node_types,
        relationship_types=relationship_types,
        patterns=patterns,
    )