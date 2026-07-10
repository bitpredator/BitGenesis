from dataclasses import dataclass, field
from typing import Any

from bitgenesis.cognition.state import CognitiveState


@dataclass(slots=True, kw_only=True)
class CognitiveContext:
    """
    Shared context for a single cognitive execution cycle.

    The context transports both intermediate cognitive results and
    references to the long-lived cognitive subsystems.
    """

    # ---------------------------------------------------------
    # Runtime state
    # ---------------------------------------------------------

    state: CognitiveState = CognitiveState.IDLE

    input_data: Any = None

    # ---------------------------------------------------------
    # Pipeline data
    # ---------------------------------------------------------

    perception: Any = None

    working_memory: list[Any] = field(default_factory=list)

    memories: list[Any] = field(default_factory=list)

    knowledge: list[Any] = field(default_factory=list)

    actions: list[Any] = field(default_factory=list)

    reasoning_result: Any = None

    plan: Any = None

    response: Any = None

    reflection: Any = None

    # ---------------------------------------------------------
    # Shared subsystem references
    # ---------------------------------------------------------

    memory_store: Any = None

    knowledge_registry: Any = None

    inference_engine: Any = None

    reflection_engine: Any = None

    response_engine: Any = None

    planner: Any = None

    executor: Any = None

    event_bus: Any = None

    # ---------------------------------------------------------
    # Helpers
    # ---------------------------------------------------------

    def update_state(self, state: CognitiveState) -> None:
        self.state = state


    def add_memory(self, memory: Any) -> None:
        self.memories.append(memory)


    def add_knowledge(self, knowledge: Any) -> None:
        self.knowledge.append(knowledge)


    def add_action(self, action: Any) -> None:
        self.actions.append(action)