from __future__ import annotations

from bitgenesis.events.event import Event
from bitgenesis.events.enums import (
    EventCategory,
    EventType,
)



class FeedbackEventFactory:
    """
    Creates runtime feedback events.
    """



    @staticmethod
    def received(
        feedback,
    ) -> Event:

        return Event(
            category=EventCategory.RUNTIME,
            type=EventType.FEEDBACK_RECEIVED,
            source="feedback_pipeline",
            payload={
                "success": feedback.execution_success,
                "actions_executed": feedback.actions_executed,
            },
        )



    @staticmethod
    def processed(
        feedback,
    ) -> Event:

        return Event(
            category=EventCategory.RUNTIME,
            type=EventType.FEEDBACK_PROCESSED,
            source="feedback_pipeline",
            payload={
                "success": feedback.success,
                "learned": feedback.learned,
            },
        )