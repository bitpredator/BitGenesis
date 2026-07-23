from __future__ import annotations


from bitgenesis.kernel.kernel import Kernel
from bitgenesis.kernel.service import KernelService



class TickService(KernelService):

    def __init__(self):

        self.counter = 0


    def start(self):
        pass


    def stop(self):
        pass


    def tick(self):

        self.counter += 1



def test_kernel_creates_runtime_loop():

    kernel = Kernel()


    assert kernel.runtime_loop is not None



def test_kernel_tick_uses_runtime_loop():

    kernel = Kernel()


    service = TickService()


    kernel.register(
        service
    )


    kernel.tick()


    assert service.counter == 1



def test_kernel_start_starts_runtime_loop():

    kernel = Kernel()


    kernel.start()


    assert kernel.running is True

    assert kernel.runtime_loop.running is True



def test_kernel_stop_stops_runtime_loop():

    kernel = Kernel()


    kernel.start()

    kernel.stop()


    assert kernel.running is False

    assert kernel.runtime_loop.running is False