from enum import Enum


class ServiceState(Enum):
    """
    Runtime lifecycle state of a Kernel service.
    """

    CREATED = "created"

    STARTING = "starting"

    READY = "ready"

    RUNNING = "running"

    STOPPING = "stopping"

    STOPPED = "stopped"

    FAILED = "failed"