from enum import Enum


class ServiceState(Enum):
    """
    Runtime lifecycle state of a Kernel service.
    """

    CREATED = "created"

    STARTING = "starting"

    READY = "ready"

    RUNNING = "running"

    STOPPING = "stoppping"

    STOPPED = "stopped"

    FAILED = "failed"