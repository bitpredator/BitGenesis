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

    # Backward compatibility with previous memory API
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

    event_bus: Any = None

    # ---------------------------------------------------------
    # State management
    # ---------------------------------------------------------

    def update_state(self, state: CognitiveState) -> None:
        """
        Updates the current cognitive state.
        """

        self.state = state

    # ---------------------------------------------------------
    # Memory helpers
    # ---------------------------------------------------------

    def add_memory(self, memory: Any) -> None:
        """
        Adds a memory item to the cognitive context.

        The memory is stored both in the legacy `memories`
        collection and in the active `working_memory`
        pipeline container.
        """

        self.memories.append(memory)

        self.working_memory.append(memory)

    def add_knowledge(self, knowledge: Any) -> None:
        """
        Adds a knowledge item to the cognitive context.

        Maintains compatibility with the previous context API.
        """

        self.knowledge.append(knowledge)


    def add_action(self, action: Any) -> None:
        """
        Adds an action produced during cognitive execution.
        """

        self.actions.append(action)