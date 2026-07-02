from bitgenesis.memory.memory_stats import MemoryStats


class MemoryLearningRules:

    @staticmethod
    def apply(memory):

        if memory.metadata is None:
            memory.metadata = {}

        if memory.tags is None:
            memory.tags = []

        # default sicuro (FONDAMENTALE)
        freq = 0

        # -----------------------------
        # 📊 LEARNING INTELLIGENTE: FREQUENZA
        # -----------------------------
        event_type = memory.metadata.get("event_type")

        if event_type:
            MemoryStats.register_event(event_type)

            freq = MemoryStats.get_frequency(event_type)

            # boost progressivo ma controllato
            memory.importance = min(
                1.0,
                memory.importance + (0.05 * freq)
            )

            memory.metadata["frequency"] = freq

        # -----------------------------
        # tagging intelligente
        # -----------------------------
        if freq >= 3:
            if "recurrent_event" not in memory.tags:
                memory.tags.append("recurrent_event")

        # -----------------------------
        # safety
        # -----------------------------
        memory.metadata["learned"] = True

        if "learned" not in memory.tags:
            memory.tags.append("learned")

        return memory