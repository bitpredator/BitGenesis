from enum import Enum


class KernelState(str, Enum):
    CREATED = "created"
    READY = "ready"
    RUNNING = "running"
    STOPPING = "stopping"
    STOPPED = "stopped"