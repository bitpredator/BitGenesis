from __future__ import annotations

import time


from bitgenesis.events.bus import EventBus
from bitgenesis.events.event import Event
from bitgenesis.events.enums import (
    EventCategory,
    EventType,
)


from bitgenesis.runtime.runtime_manager import RuntimeManager
from bitgenesis.runtime.planner import CognitiveExecutionPlanner



class RuntimeLoop:
    """
    Main execution loop for BitGenesis runtime.

    Responsibilities:

    - drive runtime ticks
    - coordinate runtime manager
    - generate cognitive execution plans
    - emit lifecycle events
    - control execution flow
    """


    def __init__(
        self,
        runtime_manager: RuntimeManager,
        event_bus: EventBus | None = None,
        interval: float = 0.1,
    ):

        self.runtime_manager = runtime_manager

        self.event_bus = event_bus

        self.interval = interval


        self.running = False

        self.tick_count = 0


        # Cognitive execution planner

        self.planner = CognitiveExecutionPlanner()

        self.last_plan = None



    # --------------------------------------------------
    # Events
    # --------------------------------------------------

    def _emit(
        self,
        event_type: EventType,
    ):

        if self.event_bus is None:
            return


        self.event_bus.publish(
            Event(
                category=EventCategory.RUNTIME,
                type=event_type,
                source=type(self).__name__,
                payload={
                    "tick": self.tick_count
                },
            )
        )



    # --------------------------------------------------
    # Lifecycle
    # --------------------------------------------------

    def start(self):

        if self.running:
            return


        self.running = True


        self._emit(
            EventType.RUNTIME_STARTED
        )



    def stop(self):

        if not self.running:
            return


        self.running = False


        self._emit(
            EventType.RUNTIME_STOPPED
        )



    # --------------------------------------------------
    # Cognitive Planning
    # --------------------------------------------------

    def plan(
        self,
        decision,
    ):
        """
        Create an execution plan from a cognitive decision.
        """


        result = self.planner.create_plan(
            decision
        )


        if result.success:

            self.last_plan = result.plan


        return result



    # --------------------------------------------------
    # Execution
    # --------------------------------------------------

    def tick(self):

        if not self.running:
            return


        self.tick_count += 1


        self.runtime_manager.tick()



        self._emit(
            EventType.RUNTIME_TICKED
        )



    def run_once(self):

        self.tick()



    def run(
        self,
        max_ticks: int | None = None,
    ):

        self.start()


        while self.running:

            self.tick()


            if (
                max_ticks is not None
                and self.tick_count >= max_ticks
            ):
                break


            time.sleep(
                self.interval
            )


        self.stop()