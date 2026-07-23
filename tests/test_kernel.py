from bitgenesis.events.event_bus import EventBus
from bitgenesis.kernel.kernel import Kernel
from bitgenesis.kernel.service import KernelService


class DummyService(KernelService):
    def __init__(self):
        super().__init__("DummyService")
        self.started = False
        self.stopped = False
        self.ticked = False

    def start(self):
        self.started = True

    def stop(self):
        self.stopped = True

    def tick(self):
        self.ticked = True


def create_kernel():
    return Kernel(EventBus())


# ---------------------------------------------------------
# Initialization
# ---------------------------------------------------------


def test_kernel_initial_state():

    kernel = create_kernel()

    assert kernel.running is False
    assert kernel.services == ()



# ---------------------------------------------------------
# Lifecycle
# ---------------------------------------------------------


def test_kernel_start():

    kernel = create_kernel()

    kernel.start()

    assert kernel.running is True



def test_kernel_stop():

    kernel = create_kernel()

    kernel.start()
    kernel.stop()

    assert kernel.running is False



def test_kernel_starts_services():

    kernel = create_kernel()

    service = DummyService()

    kernel.register(service)

    kernel.start()

    assert service.started is True



def test_kernel_stops_services():

    kernel = create_kernel()

    service = DummyService()

    kernel.register(service)

    kernel.start()
    kernel.stop()

    assert service.stopped is True



# ---------------------------------------------------------
# Services
# ---------------------------------------------------------


def test_kernel_register_service():

    kernel = create_kernel()

    service = DummyService()

    kernel.register(service)

    assert service in kernel.services



def test_kernel_unregister_service():

    kernel = create_kernel()

    service = DummyService()

    kernel.register(service)
    kernel.unregister(service)

    assert service not in kernel.services



# ---------------------------------------------------------
# Runtime
# ---------------------------------------------------------


def test_kernel_tick_calls_services():

    kernel = create_kernel()

    service = DummyService()

    kernel.register(service)

    kernel.start()
    kernel.tick()

    assert service.ticked is True