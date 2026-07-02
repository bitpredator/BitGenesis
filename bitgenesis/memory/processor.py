class MemoryProcessor:

    def process(self, memory):

        # safety init
        if memory.metadata is None:
            memory.metadata = {}

        if memory.tags is None:
            memory.tags = []

        # metadata processed
        memory.metadata["processed"] = True

        # tags idempotent
        if "memory" not in memory.tags:
            memory.tags.append("memory")

        if "processed" not in memory.tags:
            memory.tags.append("processed")

        # clamp importance
        if memory.importance is None:
            memory.importance = 0.5

        memory.importance = max(0.0, min(1.0, memory.importance))

        # clamp confidence
        if memory.confidence is None:
            memory.confidence = 1.0

        memory.confidence = max(0.0, min(1.0, memory.confidence))

        return memory