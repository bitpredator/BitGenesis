from bitgenesis.events.types import Event


class Kernel:
    def __init__(self, event_bus):
        self.event_bus = event_bus

    def start(self):
        self.event_bus.subscribe("perception.event", self.route)

    def route(self, event: Event):
        if not event.type:
            return

        self.event_bus.emit(event)