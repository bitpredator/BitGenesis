from dataclasses import dataclass, field
from typing import Any

from bitgenesis.cognition.state import CognitiveState


@dataclass(slots=True)
class CognitiveContext:
    """
    Represents the active context of a cognitive process.

    The context contains all information shared between
    cognitive pipeline stages during a single execution cycle.
    """

    state: CognitiveState = CognitiveState.IDLE

    input_data: Any = None

    memories: list[Any] = field(default_factory=list)

    knowledge: list[Any] = field(default_factory=list)

    reasoning_results: list[Any] = field(default_factory=list)

    actions: list[Any] = field(default_factory=list)

    metadata: dict[str, Any] = field(default_factory=dict)

    def update_state(self, state: CognitiveState):
        """
        Updates the current cognitive processing state.
        """

        self.state = state

    def add_memory(self, memory: Any):
        """
        Adds retrieved or generated memory information.
        """

        self.memories.append(memory)

    def add_knowledge(self, knowledge: Any):
        """
        Adds knowledge information to the context.
        """

        self.knowledge.append(knowledge)

    def add_action(self, action: Any):
        """
        Adds a planned action.
        """

        self.actions.append(action)