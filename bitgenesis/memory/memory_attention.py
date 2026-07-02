class MemoryAttention:

    @staticmethod
    def select(memories, top_k: int = 10):

        if not memories:
            return []

        def score(m):

            importance = getattr(m, "importance", 0.5)
            confidence = getattr(m, "confidence", 0.5)

            tags = getattr(m, "tags", []) or []

            tag_bonus = 0.1 if "recurrent_event" in tags else 0.0
            identity_bonus = 0.05 if "identity" in tags else 0.0

            return importance * 0.6 + confidence * 0.3 + tag_bonus + identity_bonus

        ranked = sorted(memories, key=score, reverse=True)

        return ranked[:top_k]