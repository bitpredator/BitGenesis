"""
Compatibility layer for EventBus.

This module preserves the public import path:

    bitgenesis.events.bus

while the implementation lives in:

    bitgenesis.events.event_bus
"""

from .event_bus import EventBus


__all__ = [
    "EventBus",
]