from __future__ import annotations

from bitgenesis.cognition.context import CognitiveContext

from bitgenesis.cognition.stages import (
    ConsolidationStage,
    ExecutionStage,
    KnowledgeStage,
    MemoryStage,
    PerceptionStage,
    PlanningStage,
    ReasoningStage,
    ReflectionStage,
)


class CognitiveLoop:
    """
    Executes a single cognitive pipeline.

    The CognitiveLoop is responsible only for orchestrating the
    registered cognitive stages.

    It does not implement a persistent runtime loop.
    Runtime scheduling, lifecycle and execution policies belong to
    CognitiveRuntime.

    The hook methods are intentionally designed to be overridden or
    extended in future versions (events, tracing, metrics, profiling,
    debugging, etc.).
    """

    def __init__(self, stages=None):

        self._stages = stages or [
            PerceptionStage(),
            MemoryStage(),
            KnowledgeStage(),
            ReasoningStage(),
            PlanningStage(),
            ExecutionStage(),
            ReflectionStage(),
            ConsolidationStage(),
        ]

        self._execution_count = 0

    @property
    def stages(self):

        return tuple(self._stages)

    @property
    def execution_count(self) -> int:
        """
        Number of successfully executed cognitive cycles.
        """

        return self._execution_count

    # --------------------------------------------------
    # Hooks
    # --------------------------------------------------

    def before_cycle(
        self,
        context: CognitiveContext,
    ) -> None:
        """
        Called before a cognitive cycle starts.

        Intended for subclasses and future runtime extensions.
        """

    def after_cycle(
        self,
        context: CognitiveContext,
    ) -> None:
        """
        Called after a cognitive cycle completes successfully.
        """

    def before_stage(
        self,
        stage,
        context: CognitiveContext,
    ) -> None:
        """
        Called immediately before a stage executes.
        """

    def after_stage(
        self,
        stage,
        context: CognitiveContext,
    ) -> None:
        """
        Called immediately after a stage completes.
        """

    def on_stage_failed(
        self,
        stage,
        context: CognitiveContext,
        exception: Exception,
    ) -> None:
        """
        Called when a stage raises an exception.
        """

    # --------------------------------------------------
    # Pipeline execution
    # --------------------------------------------------

    def execute(
        self,
        context: CognitiveContext,
    ) -> CognitiveContext:
        """
        Executes one complete cognitive cycle.
        """

        self.before_cycle(context)

        try:

            for stage in self._stages:

                self.before_stage(
                    stage,
                    context,
                )

                stage_name = stage.__class__.__name__

                execution = context.start_stage(
                    stage_name
                )

                try:

                    context = stage.execute(
                        context
                    )

                    context.complete_stage(
                        execution
                    )

                    self.after_stage(
                        stage,
                        context,
                    )

                except Exception as exc:

                    context.fail_stage(
                        execution,
                        exc,
                    )

                    self.on_stage_failed(
                        stage,
                        context,
                        exc,
                    )

                    raise

            context.complete_cycle()

            self._execution_count += 1

            self.after_cycle(
                context
            )

            return context

        except Exception as exc:

            context.errors.append(
                str(exc)
            )

            raise