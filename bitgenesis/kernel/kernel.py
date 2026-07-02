from bitgenesis.events.event import Event
from bitgenesis.events.enums import EventCategory


class Kernel:
    """
    Core orchestration layer of BitGenesis.
    """

    def __init__(self, event_bus):
        self.event_bus = event_bus
        self.running = False

    def start(self):
        """
        Start kernel lifecycle and register routing.
        """

        # Kernel listens to system-level events only
        self.event_bus.subscribe(
            EventCategory.SYSTEM,
            self.route
        )

        self.running = True

    def route(self, event: Event):
        """
        Central event routing logic.
        """

        if not event:
            return

        # re-dispatch event into system
        self.event_bus.publish(event)