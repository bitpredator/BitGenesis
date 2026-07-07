from bitgenesis.reasoning.reflection_engine import ReflectionEngine


class ReflectionManager:

    def __init__(
        self,
        registry,
        engine=None,
    ):

        self.registry = registry
        self.engine = engine or ReflectionEngine()

    def process(self):

        facts = list(self.registry.all())

        if not facts:
            return []

        reflections = self.engine.reflect(facts)

        added = []

        for reflection in reflections:

            if reflection in facts:
                continue

            self.registry.add(reflection)
            added.append(reflection)

        return added