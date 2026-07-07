from bitgenesis.knowledge.extractor import KnowledgeExtractor
from bitgenesis.knowledge.registry import KnowledgeRegistry


class MemoryConsolidator:

    def __init__(
        self,
        extractor=None,
        registry=None,
    ):

        self.extractor = extractor or KnowledgeExtractor()
        self.registry = registry or KnowledgeRegistry()

    def consolidate(self, episode):

        if episode is None:
            return []

        facts = []

        for memory in episode.memories:

            extracted = self.extractor.extract(memory)

            if not extracted:
                continue

            if isinstance(extracted, list):
                facts.extend(extracted)
            else:
                facts.append(extracted)

        for fact in facts:
            self.registry.add(fact)

        return facts