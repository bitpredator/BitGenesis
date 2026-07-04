from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class ActionContext:
    """
    Runtime context passed to every action handler.

    It contains all the information required to execute a single
    planning step without tightly coupling handlers to the executor.
    """

    # Current execution step
    step: Any

    # Decision that generated the plan
    decision: Any

    # Full execution plan
    plan: Any

    # Original triggering event
    event: Any = None

    # Runtime resources
    memory_store: Any = None
    graph: Any = None

    # Reserved for future extensions
    metadata: dict | None = None