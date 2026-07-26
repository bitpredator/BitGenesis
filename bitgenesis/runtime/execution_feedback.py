from __future__ import annotations

from bitgenesis.runtime.feedback_result import FeedbackResult

from bitgenesis.events.event import Event
from bitgenesis.events.enums import (
    EventCategory,
    EventType,
)

from bitgenesis.events.event_bus import EventBus



class ExecutionFeedback:
    """
    Processes execution results and produces feedback.

    Responsibilities:
    - evaluate execution outcome
    - emit feedback lifecycle events
    - prepare information for learning/memory systems
    """



    def __init__(
        self,
        event_bus: EventBus | None = None,
        memory_store=None,
    ):

        self.event_bus = event_bus

        self.memory_store = memory_store



    # --------------------------------------------------
    # Events
    # --------------------------------------------------

    def _emit(
        self,
        event_type: EventType,
        payload: dict,
    ):

        if self.event_bus is None:
            return


        self.event_bus.emit(
            Event(
                category=EventCategory.RUNTIME,
                type=event_type,
                source="execution_feedback",
                payload=payload,
            )
        )



    # --------------------------------------------------
    # Processing
    # --------------------------------------------------

    def process(
        self,
        execution_result,
    ) -> FeedbackResult:
        """
        Convert execution result into cognitive feedback.
        """


        success = execution_result.success


        feedback = FeedbackResult(
            success=True,
            execution_success=success,
            actions_executed=(
                execution_result.actions_executed
            ),
            learned=False,
            metadata={
                "success": success,
                "actions": execution_result.actions_executed,
            },
        )


        self._emit(
            EventType.EXECUTION_FEEDBACK_CREATED,
            {
                "success": success,
                "actions_executed": (
                    execution_result.actions_executed
                ),
            },
        )


        return feedback