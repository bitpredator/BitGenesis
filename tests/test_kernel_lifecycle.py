from bitgenesis.events.event_bus import EventBus
from bitgenesis.events.event import Event
from bitgenesis.events.enums import EventType, EventCategory

from bitgenesis.kernel.kernel import Kernel
from bitgenesis.kernel.service import KernelService


class DummyService(KernelService):

    def __init__(self):

        self.started = False
        self.stopped = False
        self.ticked = False


    def start(self):

        self.started = True


    def stop(self):

        self.stopped = True


    def tick(self):

        self.ticked = True



def test_kernel_start_emits_initialized_event():

    bus = EventBus()

    events = []

    bus.subscribe(
        EventType.KERNEL_INITIALIZED,
        lambda event: events.append(event)
    )


    kernel = Kernel(bus)

    kernel.start()


    assert kernel.running is True
    assert len(events) == 1

    assert events[0].type == EventType.KERNEL_INITIALIZED
    assert events[0].category == EventCategory.KERNEL



def test_kernel_start_emits_system_started_event():

    bus = EventBus()

    events = []

    bus.subscribe(
        EventType.SYSTEM_STARTED,
        lambda event: events.append(event)
    )


    kernel = Kernel(bus)

    kernel.start()


    assert len(events) == 1
    assert events[0].type == EventType.SYSTEM_STARTED



def test_kernel_starts_registered_services():

    bus = EventBus()

    kernel = Kernel(bus)

    service = DummyService()

    kernel.register(service)

    kernel.start()


    assert service.started is True



def test_kernel_tick_calls_services():

    bus = EventBus()

    kernel = Kernel(bus)

    service = DummyService()

    kernel.register(service)

    kernel.start()

    kernel.tick()


    assert service.ticked is True



def test_kernel_stop_emits_shutdown_event():

    bus = EventBus()

    events = []

    bus.subscribe(
        EventType.KERNEL_SHUTDOWN,
        lambda event: events.append(event)
    )


    kernel = Kernel(bus)

    kernel.start()

    kernel.stop()


    assert kernel.running is False

    assert len(events) == 1

    assert events[0].type == EventType.KERNEL_SHUTDOWN



def test_kernel_stops_registered_services():

    bus = EventBus()

    kernel = Kernel(bus)

    service = DummyService()

    kernel.register(service)

    kernel.start()

    kernel.stop()


    assert service.stopped is True