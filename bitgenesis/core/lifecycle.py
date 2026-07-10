from enum import Enum


class BrainState(Enum):

    IDLE = "idle"

    OBSERVING = "observing"

    RESPONDING = "responding"

    INFERRING = "inferring"

    REFLECTING = "reflecting"

    THINKING = "thinking"