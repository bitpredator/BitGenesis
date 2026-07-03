class KnowledgeGraph:

    def __init__(self):

        self.nodes = []
        self.edges = []

    def add_node(self, node):

        if node not in self.nodes:
            self.nodes.append(node)

    def add_relation(self, source, relation, target):

        self.add_node(source)
        self.add_node(target)

        edge = (source, relation, target)

        if edge not in self.edges:
            self.edges.append(edge)

    def neighbors(self, node):

        result = []

        for source, relation, target in self.edges:

            if source == node:
                result.append((relation, target))

            elif target == node:
                result.append((relation, source))

        return result

    def clear(self):

        self.nodes.clear()
        self.edges.clear()