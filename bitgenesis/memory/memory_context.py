from datetime import datetime, UTC


class MemoryContext:

    @staticmethod
    def build(memories):

        memories = list(memories)

        items = []
        total_importance = 0.0
        total_confidence = 0.0

        for memory in memories:

            total_importance += memory.importance
            total_confidence += memory.confidence

            items.append(
                {
                    "id": str(memory.id),
                    "source": memory.source,
                    "importance": memory.importance,
                    "confidence": memory.confidence,
                    "tags": list(memory.tags),
                    "metadata": dict(memory.metadata),
                    "content": memory.content,
                }
            )

        count = len(items)

        return {
            "generated_at": datetime.now(UTC).isoformat(),
            "memory_count": count,
            "average_importance": (
                total_importance / count if count else 0.0
            ),
            "average_confidence": (
                total_confidence / count if count else 0.0
            ),
            "items": items,
        }