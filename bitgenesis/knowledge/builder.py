from bitgenesis.knowledge.extractor import KnowledgeExtractor


class KnowledgeBuilder:

    def __init__(self, registry, graph):

        self.registry = registry
        self.graph = graph

    def process(self, memory):

        extracted = KnowledgeExtractor.extract(memory)

        entities = []

        for entity in extracted:

            node = self.registry.get_or_create(
                name=entity.name,
                entity_type=entity.entity_type,
                attributes=entity.attributes,
            )

            entities.append(node)

        # collega tutte le entità trovate nella memoria
        for i in range(len(entities)):
            for j in range(i + 1, len(entities)):

                self.graph.add_relation(
                    entities[i],
                    "related_to",
                    entities[j],
                )

        return entities