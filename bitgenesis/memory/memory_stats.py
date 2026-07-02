from collections import defaultdict


class MemoryStats:
    """
    Tracks frequency of event types.
    Simple in-memory learning signal.
    """

    _event_counts = defaultdict(int)

    @classmethod
    def register_event(cls, event_type: str):
        cls._event_counts[event_type] += 1

    @classmethod
    def get_frequency(cls, event_type: str) -> int:
        return cls._event_counts[event_type]

    @classmethod
    def reset(cls):
        cls._event_counts.clear()