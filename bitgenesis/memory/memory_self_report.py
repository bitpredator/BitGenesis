class MemorySelfReport:

    @staticmethod
    def generate(store) -> str:

        memories = store.all()

        total = len(memories)

        if total == 0:
            return "Memory system is empty."

        high_importance = 0
        medium_importance = 0
        low_importance = 0

        total_importance = 0
        total_confidence = 0

        recurrent = 0

        for m in memories:

            importance = getattr(m, "importance", 0)
            confidence = getattr(m, "confidence", 0)

            total_importance += importance
            total_confidence += confidence

            if importance >= 0.8:
                high_importance += 1
            elif importance >= 0.4:
                medium_importance += 1
            else:
                low_importance += 1

            tags = getattr(m, "tags", []) or []
            if "recurrent_event" in tags:
                recurrent += 1

        avg_importance = total_importance / total
        avg_confidence = total_confidence / total

        lines = [
            f"Memory system report:",
            f"- Total memories: {total}",
            f"- High importance: {high_importance}",
            f"- Medium importance: {medium_importance}",
            f"- Low importance: {low_importance}",
            f"- Recurrent patterns: {recurrent}",
            f"- Average importance: {round(avg_importance, 3)}",
            f"- Average confidence: {round(avg_confidence, 3)}",
        ]

        return "\n".join(lines)