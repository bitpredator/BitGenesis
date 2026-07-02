class MemoryNarration:

    @staticmethod
    def narrate(memory) -> str:

        if memory is None:
            return "No memory available."

        source = getattr(memory, "source", "unknown")

        metadata = memory.metadata or {}
        content = memory.content or {}

        event_type = metadata.get("event_type", "unknown_event")
        priority = metadata.get("priority", "unknown_priority")

        payload = content.get("payload", content)

        importance = getattr(memory, "importance", None)
        confidence = getattr(memory, "confidence", None)

        parts = []

        # base sentence
        parts.append(
            f"Memory event '{event_type}' processed from '{source}'"
        )

        # payload summary
        if isinstance(payload, dict) and payload:
            keys = list(payload.keys())[:3]
            parts.append(f"payload keys: {', '.join(keys)}")

        # metadata context
        parts.append(f"priority: {priority}")

        if importance is not None:
            parts.append(f"importance: {round(importance, 3)}")

        if confidence is not None:
            parts.append(f"confidence: {round(confidence, 3)}")

        return " | ".join(parts)