from bitgenesis.knowledge.entity_node import EntityNode


class KnowledgeExtractor:

    @staticmethod
    def extract(memory):

        entities = []

        content = getattr(memory, "content", {}) or {}
        payload = content.get("payload", {})

        if not isinstance(payload, dict):
            return entities

        for key, value in payload.items():

            if isinstance(value, str):

                entities.append(
                    EntityNode(
                        name=value,
                        entity_type=key,
                    )
                )

        return entities