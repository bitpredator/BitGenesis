from enum import Enum


class KernelState(Enum):
    """
    Represents the lifecycle state of the BitGenesis kernel.
    """

    CREATED = "created"

    INITIALIZING = "initializing"

    RUNNING = "running"

    STOPPING = "stopping"

    STOPPED = "stopped"

    FAILED = "failed"