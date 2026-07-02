from datetime import datetime, timezone


class MemoryDecay:
    """
    Applies time-based decay to memory importance.
    """

    @staticmethod
    def apply(memory, half_life_days: float = 7.0):
        """
        Reduces memory importance based on age.

        half_life_days:
            After this time, importance is reduced by ~50%.
        """

        if memory.metadata is None:
            memory.metadata = {}

        if memory.created_at is None:
            return memory

        now = datetime.now(timezone.utc)

        age_seconds = (now - memory.created_at).total_seconds()
        age_days = age_seconds / 86400

        # exponential decay
        decay_factor = 0.5 ** (age_days / half_life_days)

        # preserve original importance baseline if not set
        if memory.metadata.get("base_importance") is None:
            memory.metadata["base_importance"] = memory.importance

        base = memory.metadata["base_importance"]

        memory.importance = max(0.0, min(1.0, base * decay_factor))

        memory.metadata["decay_factor"] = decay_factor
        memory.metadata["age_days"] = age_days

        return memory