class MemoryProcessor:

    def process(self, memory):

        # -----------------------------
        # 🛡️ SAFETY INIT
        # -----------------------------
        if memory.metadata is None:
            memory.metadata = {}

        if memory.tags is None:
            memory.tags = []

        # -----------------------------
        # 🧾 BASE METADATA
        # -----------------------------
        memory.metadata["processed"] = True

        # -----------------------------
        # 🏷️ IDEMPOTENT TAGS
        # -----------------------------
        if "memory" not in memory.tags:
            memory.tags.append("memory")

        if "processed" not in memory.tags:
            memory.tags.append("processed")

        # -----------------------------
        # 📊 DEFAULT VALUES
        # -----------------------------
        if memory.importance is None:
            memory.importance = 0.5

        if memory.confidence is None:
            memory.confidence = 1.0

        # -----------------------------
        # 🔒 BASE CLAMP (pre-learning safety)
        # -----------------------------
        memory.importance = max(0.0, min(1.0, memory.importance))
        memory.confidence = max(0.0, min(1.0, memory.confidence))

        # -----------------------------
        # 🧠 LEARNING STEP
        # -----------------------------
        from bitgenesis.memory.learning_rules import MemoryLearningRules
        memory = MemoryLearningRules.apply(memory)

        # -----------------------------
        # 🧬 DECAY STEP
        # -----------------------------
        from bitgenesis.memory.memory_decay import MemoryDecay
        memory = MemoryDecay.apply(memory)

        # -----------------------------
        # 🔥 FINAL HARD CLAMP (anti-float drift)
        # -----------------------------
        memory.importance = round(max(0.0, min(1.0, memory.importance)), 6)
        memory.confidence = round(max(0.0, min(1.0, memory.confidence)), 6)

        return memory