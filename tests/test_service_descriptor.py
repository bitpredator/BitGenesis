from bitgenesis.kernel.service_manager import ServiceManager
from bitgenesis.kernel.service import KernelService
from bitgenesis.kernel.descriptor import ServiceDescriptor



# --------------------------------------------------
# Test Services
# --------------------------------------------------


class BasicService(KernelService):

    def start(self):
        pass

    def stop(self):
        pass

    def tick(self):
        pass



class PriorityService(KernelService):

    def __init__(
        self,
        name,
        events,
    ):
        self.name = name
        self.events = events


    def start(self):

        self.events.append(
            self.name
        )


    def stop(self):
        pass


    def tick(self):
        pass



class DisabledService(KernelService):

    def __init__(
        self,
        events,
    ):
        self.events = events


    def start(self):

        self.events.append(
            "started"
        )


    def stop(self):
        pass



# --------------------------------------------------
# Descriptor creation
# --------------------------------------------------


def test_service_descriptor_default_creation():


    manager = ServiceManager()


    service = BasicService()


    manager.register(
        service
    )


    descriptor = manager.descriptor(
        BasicService
    )


    assert descriptor is not None

    assert descriptor.name == (
        "BasicService"
    )

    assert descriptor.version == (
        "1.0.0"
    )

    assert descriptor.priority == 100

    assert descriptor.auto_start is True



# --------------------------------------------------
# Custom descriptor
# --------------------------------------------------


def test_service_custom_descriptor():


    manager = ServiceManager()


    service = BasicService()


    descriptor = ServiceDescriptor(
        name="brain",
        version="2.0.0",
        priority=5,
        tags=(
            "core",
        ),
    )


    manager.register(
        service,
        descriptor,
    )


    stored = manager.descriptor(
        BasicService
    )


    assert stored.name == "brain"

    assert stored.version == "2.0.0"

    assert stored.priority == 5

    assert stored.tags == (
        "core",
    )



# --------------------------------------------------
# Priority startup
# --------------------------------------------------


def test_service_priority_start_order():


    events = []


    manager = ServiceManager()



    first = PriorityService(
        "first",
        events,
    )


    second = PriorityService(
        "second",
        events,
    )



    manager.register(
        first,
        ServiceDescriptor(
            name="first",
            priority=200,
        ),
    )


    manager.register(
        second,
        ServiceDescriptor(
            name="second",
            priority=10,
        ),
    )



    manager.start_all()



    assert events == [
        "second",
        "first",
    ]



# --------------------------------------------------
# Auto start disabled
# --------------------------------------------------


def test_service_auto_start_disabled():


    events = []


    manager = ServiceManager()



    service = DisabledService(
        events
    )


    manager.register(
        service,
        ServiceDescriptor(
            name="disabled",
            auto_start=False,
        ),
    )



    manager.start_all()



    assert events == []



# --------------------------------------------------
# Shutdown reverse priority
# --------------------------------------------------


def test_service_stop_reverse_priority():


    events = []


    class StopService(KernelService):


        def __init__(
            self,
            name,
        ):
            self.name = name


        def start(self):
            pass


        def stop(self):

            events.append(
                self.name
            )


        def tick(self):
            pass



    manager = ServiceManager()



    manager.register(
        StopService("low"),
        ServiceDescriptor(
            name="low",
            priority=10,
        ),
    )


    manager.register(
        StopService("high"),
        ServiceDescriptor(
            name="high",
            priority=100,
        ),
    )



    manager.stop_all()



    assert events == [
        "high",
        "low",
    ]