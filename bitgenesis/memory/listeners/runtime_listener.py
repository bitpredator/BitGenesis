from __future__ import annotations

from bitgenesis.events.event import Event
from bitgenesis.events.enums import (
    EventCategory,
    EventType,
)

from bitgenesis.memory.factory import MemoryFactory


class RuntimeEpisodeListener:
    """
    Listens for runtime execution events and converts them
    into episodic memories.

    The listener is intentionally lightweight and only
    translates runtime events into Memory objects.
    """

    _SUPPORTED_EVENTS = {
        EventType.ACTION_STARTED,
        EventType.ACTION_COMPLETED,
        EventType.ACTION_FAILED,
        EventType.EXECUTION_STARTED,
        EventType.EXECUTION_COMPLETED,
        EventType.EXECUTION_FAILED,
    }

    def __init__(
        self,
        memory_store,
        episode_manager=None,
    ):

        self.memory_store = memory_store
        self.episode_manager = episode_manager

    def handle(
        self,
        event: Event,
    ) -> None:
        """
        Handles runtime events published on the EventBus.
        """

        if event.category is not EventCategory.RUNTIME:
            return

        if event.type not in self._SUPPORTED_EVENTS:
            return

        memory = MemoryFactory.from_event(event)

        self.memory_store.add(memory)

        if self.episode_manager is not None:

            ingest = getattr(
                self.episode_manager,
                "ingest",
                None,
            )

            if callable(ingest):
                ingest(memory)