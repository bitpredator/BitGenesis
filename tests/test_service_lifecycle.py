from bitgenesis.kernel.service_lifecycle import (
    ServiceLifecycle,
    InvalidServiceTransition,
)

from bitgenesis.kernel.service_state import ServiceState



def test_valid_service_transition():

    state = ServiceLifecycle.transition(
        ServiceState.CREATED,
        ServiceState.STARTING,
    )

    assert state == ServiceState.STARTING



def test_running_to_stopping():

    state = ServiceLifecycle.transition(
        ServiceState.RUNNING,
        ServiceState.STOPPING,
    )

    assert state == ServiceState.STOPPING



def test_invalid_transition():

    try:

        ServiceLifecycle.transition(
            ServiceState.CREATED,
            ServiceState.STOPPED,
        )

        assert False

    except InvalidServiceTransition:

        assert True