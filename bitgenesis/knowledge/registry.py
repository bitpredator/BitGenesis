from bitgenesis.knowledge.entity_node import EntityNode


class KnowledgeRegistry:

    def __init__(self):

        self._entities = {}

    def get_or_create(
        self,
        name: str,
        entity_type: str = "generic",
        attributes: dict | None = None,
    ):

        key = name.strip().lower()

        if key in self._entities:
            return self._entities[key]

        entity = EntityNode(
            name=name,
            entity_type=entity_type,
            attributes=attributes or {},
        )

        self._entities[key] = entity

        return entity

    def get(self, name: str):

        return self._entities.get(name.strip().lower())

    def exists(self, name: str):

        return name.strip().lower() in self._entities

    def all(self):

        return list(self._entities.values())

    def count(self):

        return len(self._entities)

    def clear(self):

        self._entities.clear()