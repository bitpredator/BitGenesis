from bitgenesis.kernel.kernel import Kernel
from bitgenesis.events.event_bus import EventBus
from bitgenesis.kernel.state import KernelState


print("=== BitGenesis Kernel Boot Test ===")


bus = EventBus()


kernel = Kernel(
    bus=bus,
)


print("Kernel created")
print("Initial state:", kernel.state)


assert kernel.state == KernelState.CREATED
assert kernel.running is False


kernel.start()


print("Kernel started")
print("Current state:", kernel.state)


assert kernel.running is True
assert kernel.state == KernelState.RUNNING


assert kernel.brain is not None


print(
    "Brain initialized:",
    type(kernel.brain).__name__,
)


kernel.stop()


print("Kernel stopped")
print("Current state:", kernel.state)


assert kernel.running is False
assert kernel.state == KernelState.STOPPED


print("=== Kernel Boot Test OK ===")