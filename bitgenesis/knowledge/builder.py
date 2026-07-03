from bitgenesis.knowledge.extractor import KnowledgeExtractor
from bitgenesis.knowledge.relation_mapper import RelationMapper


class KnowledgeBuilder:

    def __init__(self, registry, graph):

        self.registry = registry
        self.graph = graph

    def process(self, memory):

        extracted = KnowledgeExtractor.extract(memory)

        if not extracted:
            return []

        entities = []

        for entity in extracted:

            node = self.registry.get_or_create(
                name=entity.name,
                entity_type=entity.entity_type,
                attributes=entity.attributes,
            )

            entities.append(node)

        # Individua il progetto principale
        project = None

        for entity in entities:
            if entity.entity_type == "project":
                project = entity
                break

        if project is None:
            return entities

        # Costruisce le relazioni semantiche
        for entity in entities:

            if entity is project:
                continue

            relation = RelationMapper.relation_for(entity.entity_type)

            if relation in ("creator_of", "author_of", "developer_of"):
                self.graph.add_relation(
                    entity,
                    relation,
                    project,
                )

            elif relation == "written_in":
                self.graph.add_relation(
                    project,
                    relation,
                    entity,
                )

            else:
                self.graph.add_relation(
                    project,
                    relation,
                    entity,
                )

        return entities