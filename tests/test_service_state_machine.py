from bitgenesis.kernel.service_lifecycle import (
    ServiceLifecycle,
    InvalidServiceTransition,
)

from bitgenesis.kernel.service_state import ServiceState



def test_initial_state_is_created():

    state = ServiceState.CREATED

    assert state == ServiceState.CREATED



def test_created_to_starting_transition():

    result = ServiceLifecycle.transition(
        ServiceState.CREATED,
        ServiceState.STARTING,
    )

    assert result == ServiceState.STARTING



def test_starting_to_ready_transition():

    result = ServiceLifecycle.transition(
        ServiceState.STARTING,
        ServiceState.READY,
    )

    assert result == ServiceState.READY



def test_ready_to_running_transition():

    result = ServiceLifecycle.transition(
        ServiceState.READY,
        ServiceState.RUNNING,
    )

    assert result == ServiceState.RUNNING



def test_running_to_stopping_transition():

    result = ServiceLifecycle.transition(
        ServiceState.RUNNING,
        ServiceState.STOPPING,
    )

    assert result == ServiceState.STOPPING



def test_stopping_to_stopped_transition():

    result = ServiceLifecycle.transition(
        ServiceState.STOPPING,
        ServiceState.STOPPED,
    )

    assert result == ServiceState.STOPPED



def test_failed_transition_is_allowed():

    result = ServiceLifecycle.transition(
        ServiceState.STARTING,
        ServiceState.FAILED,
    )

    assert result == ServiceState.FAILED



def test_invalid_created_to_stopped_transition():

    try:

        ServiceLifecycle.transition(
            ServiceState.CREATED,
            ServiceState.STOPPED,
        )

        assert False, "Transition should have failed"


    except InvalidServiceTransition:

        assert True



def test_invalid_stopped_to_running_transition():

    try:

        ServiceLifecycle.transition(
            ServiceState.STOPPED,
            ServiceState.RUNNING,
        )

        assert False, "Transition should have failed"


    except InvalidServiceTransition:

        assert True



def test_can_transition_helper():

    assert ServiceLifecycle.can_transition(
        ServiceState.CREATED,
        ServiceState.STARTING,
    )


    assert not ServiceLifecycle.can_transition(
        ServiceState.CREATED,
        ServiceState.RUNNING,
    )