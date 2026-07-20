from __future__ import annotations


from bitgenesis.kernel.service_manager import ServiceManager
from bitgenesis.kernel.service import KernelService



# ======================================================
# Dummy Services
# ======================================================


class DummyService(KernelService):

    def __init__(self):

        self.started = False
        self.stopped = False
        self.ticks = 0


    def start(self):

        self.started = True


    def stop(self):

        self.stopped = True


    def tick(self):

        self.ticks += 1



class FirstService(KernelService):

    def __init__(self, events):

        self.events = events


    def stop(self):

        self.events.append(
            "first"
        )



class SecondService(KernelService):

    def __init__(self, events):

        self.events = events


    def stop(self):

        self.events.append(
            "second"
        )



# ======================================================
# Register
# ======================================================


def test_service_manager_register():

    manager = ServiceManager()

    service = DummyService()


    manager.register(
        service
    )


    assert service in manager.all()



# ======================================================
# Unregister
# ======================================================


def test_service_manager_unregister():

    manager = ServiceManager()

    service = DummyService()


    manager.register(
        service
    )


    manager.unregister(
        service
    )


    assert service not in manager.all()



# ======================================================
# Get
# ======================================================


def test_service_manager_get():

    manager = ServiceManager()

    service = DummyService()


    manager.register(
        service
    )


    result = manager.get(
        DummyService
    )


    assert result is service



# ======================================================
# Lifecycle start
# ======================================================


def test_service_manager_start_all():

    manager = ServiceManager()

    service = DummyService()


    manager.register(
        service
    )


    manager.start_all()


    assert service.started is True



# ======================================================
# Lifecycle stop
# ======================================================


def test_service_manager_stop_all():

    manager = ServiceManager()

    service = DummyService()


    manager.register(
        service
    )


    manager.stop_all()


    assert service.stopped is True



# ======================================================
# Runtime tick
# ======================================================


def test_service_manager_tick_all():

    manager = ServiceManager()

    service = DummyService()


    manager.register(
        service
    )


    manager.tick_all()


    assert service.ticks == 1



# ======================================================
# Shutdown order
# ======================================================


def test_service_manager_shutdown_order():

    events = []


    manager = ServiceManager()


    manager.register(
        FirstService(events)
    )

    manager.register(
        SecondService(events)
    )


    manager.stop_all()


    assert events == [
        "second",
        "first",
    ]