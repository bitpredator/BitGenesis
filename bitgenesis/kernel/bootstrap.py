from bitgenesis.core.event_bus import EventBus
from bitgenesis.core.kernel import Kernel


def bootstrap():
    bus = EventBus()
    kernel = Kernel(bus)

    kernel.start()

    return bus, kernel