"""
Legacy compatibility module.

The BitGenesis event system was migrated to:

- bitgenesis.events.event.Event
- bitgenesis.events.enums.EventType
- bitgenesis.events.enums.EventCategory

This module only re-exports the new implementation.
"""


from bitgenesis.events.event import Event

from bitgenesis.events.enums import (
    EventType,
    EventCategory,
    EventPriority,
)


__all__ = [
    "Event",
    "EventType",
    "EventCategory",
    "EventPriority",
]