from enum import Enum


class CognitiveState(str, Enum):
    """
    Represents the current state of the cognitive runtime.
    """

    INITIALIZING = "initializing"

    IDLE = "idle"

    PERCEIVING = "perceiving"

    CONTEXTUALIZING = "contextualizing"

    RETRIEVING_MEMORY = "retrieving_memory"

    INTEGRATING_KNOWLEDGE = "integrating_knowledge"

    REASONING = "reasoning"

    PLANNING = "planning"

    EXECUTING = "executing"

    REFLECTING = "reflecting"

    CONSOLIDATING = "consolidating"

    COMPLETED = "completed"

    FAILED = "failed"