from enum import Enum


class BrainState(str, Enum):

    IDLE = "idle"

    OBSERVING = "observing"

    CONSOLIDATING = "consolidating"

    INFERRING = "inferring"

    REFLECTING = "reflecting"

    RESPONDING = "responding"

    SHUTDOWN = "shutdown"