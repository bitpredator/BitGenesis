from bitgenesis.memory.memory_similarity import MemorySimilarity


class MemoryRetrieval:

    @staticmethod
    def retrieve(event, memories, top_k: int = 10):

        scored = []

        for memory in memories:

            score = 0.0

            metadata = getattr(memory, "metadata", {}) or {}
            content = getattr(memory, "content", {}) or {}

            # -------------------------
            # Event Type
            # -------------------------
            if metadata.get("event_type") == event.type.value:
                score += 5.0

            # -------------------------
            # Category
            # -------------------------
            if metadata.get("event_category") == event.category.value:
                score += 3.0

            # -------------------------
            # Source
            # -------------------------
            if getattr(memory, "source", None) == event.source:
                score += 2.0

            # -------------------------
            # Semantic similarity
            # -------------------------
            payload = content.get("payload", {})

            score += MemorySimilarity.score(
                event.payload,
                payload,
            )

            # -------------------------
            # Importance
            # -------------------------
            score += getattr(memory, "importance", 0.5) * 2.0

            # -------------------------
            # Confidence
            # -------------------------
            score += getattr(memory, "confidence", 1.0)

            scored.append((score, memory))

        scored.sort(
            key=lambda item: item[0],
            reverse=True,
        )

        return [memory for _, memory in scored[:top_k]]