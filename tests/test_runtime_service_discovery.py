from bitgenesis.runtime.runtime_manager import (
    RuntimeManager,
)



class DummyRuntimeService:
    """
    Fake runtime service.
    """

    def __init__(self):

        self.started = False

        self.executed = False

        self.stopped = False



    def start(
        self,
        context,
    ):

        self.started = True



    def execute(
        self,
        context,
    ):

        self.executed = True

        return "ok"



    def stop(
        self,
        context,
    ):

        self.stopped = True




def test_runtime_manager_register_service():

    runtime = RuntimeManager()


    service = DummyRuntimeService()


    descriptor = runtime.register_service(
        service,
        name="dummy",
    )


    assert descriptor.name == "dummy"


    found = runtime.discover_service(
        "dummy"
    )


    assert found is not None

    assert found.service is service




def test_runtime_manager_service_discovery_list():

    runtime = RuntimeManager()


    runtime.register_service(
        DummyRuntimeService(),
        name="one",
    )


    runtime.register_service(
        DummyRuntimeService(),
        name="two",
    )


    services = runtime.discover_services()


    assert len(services) == 2




def test_runtime_manager_start_service_lifecycle():

    runtime = RuntimeManager()


    service = DummyRuntimeService()


    runtime.register_service(
        service
    )


    runtime.start()


    assert runtime.running is True

    assert service.started is True




def test_runtime_manager_tick_executes_services():

    runtime = RuntimeManager()


    service = DummyRuntimeService()


    runtime.register_service(
        service
    )


    runtime.start()


    result = runtime.tick()


    assert result is not None

    assert result.services_executed == 1

    assert service.executed is True




def test_runtime_manager_stop_service_lifecycle():

    runtime = RuntimeManager()


    service = DummyRuntimeService()


    runtime.register_service(
        service
    )


    runtime.start()

    runtime.stop()


    assert runtime.running is False

    assert service.stopped is True




def test_runtime_manager_unregister_service():

    runtime = RuntimeManager()


    runtime.register_service(
        DummyRuntimeService(),
        name="dummy",
    )


    removed = runtime.unregister_service(
        "dummy"
    )


    assert removed is True


    assert (
        runtime.discover_service(
            "dummy"
        )
        is None
    )