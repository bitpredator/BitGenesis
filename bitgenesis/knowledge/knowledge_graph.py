from bitgenesis.knowledge.entity_node import EntityNode
from bitgenesis.knowledge.relation import Relation


class KnowledgeGraph:

    def __init__(self):

        self.nodes = {}
        self.relations = []

    # -------------------------
    # Nodes
    # -------------------------

    def add_node(self, node: EntityNode):

        self.nodes[node.id] = node

        return node

    def get_node(self, node_id):

        return self.nodes.get(node_id)

    def all_nodes(self):

        return list(self.nodes.values())

    # -------------------------
    # Relations
    # -------------------------

    def add_relation(self, relation: Relation):

        self.relations.append(relation)

        return relation

    def all_relations(self):

        return list(self.relations)

    # -------------------------
    # Graph queries
    # -------------------------

    def neighbors(self, node_id):

        result = []

        for relation in self.relations:

            if relation.source == node_id:

                node = self.get_node(relation.target)

                if node is not None:
                    result.append(node)

        return result