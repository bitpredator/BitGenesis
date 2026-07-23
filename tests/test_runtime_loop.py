from __future__ import annotations

import time


from bitgenesis.kernel.runtime_loop import RuntimeLoop
from bitgenesis.kernel.service import KernelService
from bitgenesis.kernel.service_manager import ServiceManager



# --------------------------------------------------
# Mock service
# --------------------------------------------------


class CounterService(KernelService):

    def __init__(self):

        self.ticks = 0


    def start(self):
        pass


    def stop(self):
        pass


    def tick(self):

        self.ticks += 1



# --------------------------------------------------
# Tests
# --------------------------------------------------


def test_runtime_loop_step_executes_service_tick():

    manager = ServiceManager()

    service = CounterService()


    manager.register(
        service
    )


    loop = RuntimeLoop(
        service_manager=manager,
    )


    loop.step()


    assert service.ticks == 1



def test_runtime_loop_executes_cognitive_step():

    manager = ServiceManager()


    calls = []


    def cognitive_step():

        calls.append(
            "step"
        )


    loop = RuntimeLoop(
        service_manager=manager,
        cognitive_step=cognitive_step,
    )


    loop.step()


    assert calls == [
        "step"
    ]



def test_runtime_loop_start_and_stop():

    manager = ServiceManager()


    service = CounterService()


    manager.register(
        service
    )


    loop = RuntimeLoop(
        service_manager=manager,
        interval=0.01,
    )


    assert loop.running is False


    loop.start()


    time.sleep(
        0.05
    )


    assert loop.running is True

    assert service.ticks > 0


    loop.stop()


    assert loop.running is False



def test_runtime_loop_double_start_is_safe():

    manager = ServiceManager()


    loop = RuntimeLoop(
        service_manager=manager,
        interval=0.01,
    )


    loop.start()

    first_thread = loop._thread


    loop.start()


    assert loop._thread is first_thread


    loop.stop()



def test_runtime_loop_stop_without_start():

    manager = ServiceManager()


    loop = RuntimeLoop(
        service_manager=manager,
    )


    loop.stop()


    assert loop.running is False