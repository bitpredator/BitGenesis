class KnowledgeQuery:

    def __init__(self, graph):

        self.graph = graph

    def neighbors(self, entity):

        return self.graph.neighbors(entity)

    def find_by_name(self, name):

        for node in self.graph.nodes:

            if node.name == name:
                return node

        return None

    def relations_of(self, name):

        node = self.find_by_name(name)

        if node is None:
            return []

        return self.graph.neighbors(node)

    def exists(self, name):

        return self.find_by_name(name) is not None