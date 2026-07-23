from bitgenesis.kernel.service_manager import ServiceManager
from bitgenesis.kernel.service import KernelService
from bitgenesis.kernel.service_state import ServiceState



class TestService(KernelService):

    def start(self):
        pass


    def stop(self):
        pass


    def tick(self):
        pass



def test_service_state_after_start():

    manager = ServiceManager()

    service = TestService()


    manager.register(
        service
    )


    manager.start_all()


    assert manager.state(
        TestService
    ) == ServiceState.RUNNING



def test_service_state_after_stop():

    manager = ServiceManager()

    service = TestService()


    manager.register(
        service
    )


    manager.start_all()

    manager.stop_all()


    assert manager.state(
        TestService
    ) == ServiceState.STOPPED



def test_running_services():

    manager = ServiceManager()

    service = TestService()


    manager.register(
        service
    )


    manager.start_all()


    assert service in manager.running_services()



def test_failed_service_state():

    class BrokenService(KernelService):

        def start(self):

            raise RuntimeError(
                "fail"
            )


    manager = ServiceManager()

    service = BrokenService()


    manager.register(
        service
    )


    try:
        manager.start_all()
    except RuntimeError:
        pass


    assert manager.state(
        BrokenService
    ) == ServiceState.FAILED