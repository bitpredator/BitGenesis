from bitgenesis.knowledge.knowledge_query import KnowledgeQuery


class KnowledgeReasoner:

    def __init__(self, graph):

        self.query = KnowledgeQuery(graph)

    def answer(self, subject: str):

        if not self.query.exists(subject):
            return None

        relations = self.query.relations_of(subject)

        result = []

        for relation, target in relations:

            result.append(
                {
                    "relation": relation,
                    "target": target.name,
                    "type": target.entity_type,
                }
            )

        return result

    def has_knowledge(self, subject: str):

        return self.query.exists(subject)