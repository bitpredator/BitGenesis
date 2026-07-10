from dataclasses import dataclass, field
from datetime import datetime, UTC
from typing import Any
from uuid import uuid4

from bitgenesis.cognition.state import CognitiveState


@dataclass(slots=True, kw_only=True)
class CognitiveContext:
    """
    Shared context for a single cognitive execution cycle.

    The context transports both intermediate cognitive results,
    references to long-lived cognitive subsystems and runtime
    execution metadata.
    """

    # ---------------------------------------------------------
    # Runtime state
    # ---------------------------------------------------------

    state: CognitiveState = CognitiveState.IDLE

    input_data: Any = None

    cycle_id: str = field(
        default_factory=lambda: str(uuid4())
    )

    started_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    completed_at: datetime | None = None

    # ---------------------------------------------------------
    # Runtime observability
    # ---------------------------------------------------------

    stage_history: list[dict[str, Any]] = field(
        default_factory=list
    )

    errors: list[str] = field(
        default_factory=list
    )

    # ---------------------------------------------------------
    # Pipeline data
    # ---------------------------------------------------------

    perception: Any = None

    working_memory: list[Any] = field(
        default_factory=list
    )

    memories: list[Any] = field(
        default_factory=list
    )

    knowledge: list[Any] = field(
        default_factory=list
    )

    actions: list[Any] = field(
        default_factory=list
    )

    reasoning_result: Any = None

    plan: Any = None

    response: Any = None

    reflection: Any = None

    # ---------------------------------------------------------
    # Shared subsystem references
    # ---------------------------------------------------------

    memory_store: Any = None

    memory_factory: Any = None

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

    def update_state(
        self,
        state: CognitiveState
    ) -> None:

        self.state = state


    def add_memory(
        self,
        memory: Any
    ) -> None:

        self.memories.append(
            memory
        )


    def add_knowledge(
        self,
        knowledge: Any
    ) -> None:

        self.knowledge.append(
            knowledge
        )


    def add_action(
        self,
        action: Any
    ) -> None:

        self.actions.append(
            action
        )


    # ---------------------------------------------------------
    # Cognitive cycle tracking
    # ---------------------------------------------------------

    def start_stage(
        self,
        stage_name: str
    ) -> dict[str, Any]:

        execution = {
            "stage": stage_name,
            "started_at": datetime.now(UTC),
            "completed_at": None,
            "success": False,
            "error": None,
        }

        self.stage_history.append(
            execution
        )

        return execution


    def complete_stage(
        self,
        execution: dict[str, Any]
    ) -> None:

        execution["completed_at"] = datetime.now(UTC)

        execution["success"] = True


    def fail_stage(
        self,
        execution: dict[str, Any],
        error: Exception
    ) -> None:

        execution["completed_at"] = datetime.now(UTC)

        execution["error"] = str(error)

        self.errors.append(
            str(error)
        )


    def complete_cycle(self) -> None:

        self.completed_at = datetime.now(UTC)