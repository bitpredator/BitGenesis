from __future__ import annotations

from bitgenesis.kernel.service_state import ServiceState



class InvalidServiceTransition(Exception):
    """
    Raised when a service lifecycle transition is not allowed.
    """

    pass



class ServiceLifecycle:


    _transitions = {

        ServiceState.CREATED: {
            ServiceState.STARTING,
            ServiceState.FAILED,
        },

        ServiceState.STARTING: {
            ServiceState.READY,
            ServiceState.FAILED,
        },

        ServiceState.READY: {
            ServiceState.RUNNING,
            ServiceState.STOPPING,
            ServiceState.FAILED,
        },

        ServiceState.RUNNING: {
            ServiceState.STOPPING,
            ServiceState.FAILED,
        },

        ServiceState.STOPPING: {
            ServiceState.STOPPED,
            ServiceState.FAILED,
        },

        ServiceState.STOPPED: set(),

        ServiceState.FAILED: {
            ServiceState.STOPPING,
        },
    }



    @classmethod
    def can_transition(
        cls,
        current: ServiceState,
        target: ServiceState,
    ) -> bool:

        return target in cls._transitions.get(
            current,
            set(),
        )



    @classmethod
    def transition(
        cls,
        current: ServiceState,
        target: ServiceState,
    ) -> ServiceState:


        if not cls.can_transition(
            current,
            target,
        ):

            raise InvalidServiceTransition(
                f"Invalid transition: "
                f"{current.value} -> {target.value}"
            )


        return target