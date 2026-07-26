from __future__ import annotations

from bitgenesis.runtime.feedback_handler import FeedbackHandler
from bitgenesis.runtime.feedback_event import FeedbackEventFactory

from bitgenesis.events.event_bus import EventBus



class FeedbackPipeline:
    """
    Execution feedback processing pipeline.

    Flow:

    ExecutionResult
            |
            v
    ExecutionFeedback
            |
            v
    FeedbackPipeline
            |
            v
    FeedbackHandler
    """



    def __init__(
        self,
        handler: FeedbackHandler | None = None,
        event_bus: EventBus | None = None,
    ):

        self.handler = (
            handler
            or FeedbackHandler()
        )

        self.event_bus = event_bus



    # --------------------------------------------------
    # Events
    # --------------------------------------------------

    def _emit(
        self,
        event,
    ):

        if self.event_bus is None:
            return

        self.event_bus.emit(
            event
        )



    # --------------------------------------------------
    # Processing
    # --------------------------------------------------

    def process(
        self,
        feedback,
    ):

        self._emit(
            FeedbackEventFactory.received(
                feedback
            )
        )


        result = self.handler.process(
            feedback
        )


        self._emit(
            FeedbackEventFactory.processed(
                result
            )
        )


        return result