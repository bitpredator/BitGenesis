from collections import defaultdict
from typing import Callable, Dict, List
from bitgenesis.events.types import Event


class EventBus:
    def __init__(self):
        self.listeners: Dict[str, List[Callable]] = defaultdict(list)
        self.event_log = []

    def subscribe(self, event_type: str, handler: Callable):
        self.listeners[event_type].append(handler)

    def emit(self, event: Event):
        self._log(event)

        handlers = self.listeners.get(event.type, [])
        for handler in handlers:
            handler(event)

    def _log(self, event: Event):
        self.event_log.append(event)