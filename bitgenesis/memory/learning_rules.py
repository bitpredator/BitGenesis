class MemoryLearningRules:

    @staticmethod
    def apply(memory):
        # inizializzazione sicura (come fai nel processor)
        if memory.metadata is None:
            memory.metadata = {}

        if memory.tags is None:
            memory.tags = []

        # segna che la memoria è stata "analizzata"
        memory.metadata["learned"] = True

        # aggiunge un tag
        if "learned" not in memory.tags:
            memory.tags.append("learned")

        return memory