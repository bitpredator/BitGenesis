from __future__ import annotations

import time


from bitgenesis.kernel.kernel import Kernel
from bitgenesis.kernel.service import KernelService
from bitgenesis.events.event_bus import EventBus



print("=== Kernel Runtime Integration Test ===")



# --------------------------------------------------
# Test service
# --------------------------------------------------

class RuntimeTestService(KernelService):

    def __init__(self):

        super().__init__(
            "runtime_test_service"
        )

        self.ticks = 0



    def tick(self):

        self.ticks += 1




# --------------------------------------------------
# Kernel
# --------------------------------------------------

bus = EventBus()


kernel = Kernel(
    bus=bus,
)



service = RuntimeTestService()



kernel.register(
    service
)



print(
    "Service registered"
)



# --------------------------------------------------
# Start
# --------------------------------------------------

kernel.start()


print(
    "Kernel state:",
    kernel.state,
)



assert kernel.running is True


assert service.running is True



# lascia lavorare il runtime loop

time.sleep(
    0.5
)



print(
    "Service ticks:",
    service.ticks,
)



assert service.ticks > 0


assert kernel.runtime_loop.tick_count > 0



# --------------------------------------------------
# Stop
# --------------------------------------------------

kernel.stop()



print(
    "Kernel stopped:",
    kernel.state,
)



assert kernel.running is False


assert service.running is False



print(
    "=== Kernel Runtime Integration Test OK ==="
)