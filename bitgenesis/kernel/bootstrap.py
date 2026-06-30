from bitgenesis.events.event_bus import EventBus
from bitgenesis.kernel.kernel import Kernel


def bootstrap():
    bus = EventBus()
    kernel = Kernel(bus)

    kernel.start()

    return bus, kernel