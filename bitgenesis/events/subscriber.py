"""
Subscriber interface for the BitGenesis Event System.
"""

from typing import Protocol, runtime_checkable

from .event import Event


@runtime_checkable
class EventSubscriber(Protocol):
    """
    Defines the contract for every event subscriber.

    Any component that wants to receive events from the EventBus
    must implement this protocol.
    """

    def handle(self, event: Event) -> None:
        """
        Handle a published event.
        """
        ...