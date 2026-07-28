from bitgenesis.kernel.kernel import Kernel
from bitgenesis.kernel.service import KernelService
from bitgenesis.kernel.service_state import ServiceState


class TestRuntimeService(KernelService):

    def __init__(self):

        super().__init__(
            name="test_runtime_service"
        )

        self.started = False
        self.ticks = 0
        self.stopped = False


    def start(self):

        super().start()

        self.started = True


    def tick(self):

        self.ticks += 1


    def stop(self):

        super().stop()

        self.stopped = True



print("=== Service Lifecycle Functional Test ===")


kernel = Kernel()


service = TestRuntimeService()


kernel.register(
    service
)


print("Service registered")


kernel.start()


print("Kernel running")


assert service.running is True
assert service.started is True


kernel.tick()
kernel.tick()


print(
    "Ticks:",
    service.ticks
)


assert service.ticks >= 2


state = kernel.service_manager.state(
    type(service)
)


print(
    "Service state:",
    state
)


assert state == ServiceState.RUNNING


kernel.stop()


print("Kernel stopped")


assert service.stopped is True


print("=== Service Lifecycle Test OK ===")