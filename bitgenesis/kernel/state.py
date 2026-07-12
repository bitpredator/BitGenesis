from enum import Enum


class KernelState(str, Enum):

    STOPPED = "stopped"

    STARTING = "starting"

    RUNNING = "running"

    PAUSED = "paused"

    SHUTTING_DOWN = "shutting_down"