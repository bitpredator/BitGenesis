from __future__ import annotations

import time
import threading

from datetime import datetime, UTC
from typing import Callable


from bitgenesis.kernel.service_manager import ServiceManager

from bitgenesis.events.event_bus import EventBus
from bitgenesis.events.event import Event
from bitgenesis.events.enums import (
    EventCategory,
    EventType,
)



class RuntimeLoop:
    """
    Main execution loop for BitGenesis kernel runtime.

    Responsibilities:

    - maintain execution lifecycle
    - tick registered services
    - execute cognitive runtime steps
    - emit runtime lifecycle events
    - provide controlled shutdown
    """



    def __init__(
        self,
        service_manager: ServiceManager,
        cognitive_step: Callable[[], None] | None = None,
        interval: float = 0.1,
        event_bus: EventBus | None = None,
    ):


        self.service_manager = service_manager

        self.cognitive_step = cognitive_step

        self.interval = interval

        self.event_bus = event_bus


        self._running = False

        self._thread: threading.Thread | None = None

        self._stop_event = threading.Event()


        self.tick_count = 0

        self.last_tick_time: datetime | None = None



    # --------------------------------------------------
    # State
    # --------------------------------------------------

    @property
    def running(
        self,
    ) -> bool:

        return self._running



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
                    "tick": self.tick_count,
                },
            )
        )



    # --------------------------------------------------
    # Lifecycle
    # --------------------------------------------------

    def start(
        self,
    ):

        if self._running:
            return


        self._running = True

        self._stop_event.clear()


        self._emit(
            EventType.RUNTIME_STARTED
        )


        self._thread = threading.Thread(
            target=self._run,
            name="BitGenesisRuntimeLoop",
            daemon=True,
        )


        self._thread.start()



    def stop(
        self,
    ):

        if not self._running:
            return


        self._running = False


        self._stop_event.set()


        if self._thread:

            self._thread.join(
                timeout=2.0
            )


            self._thread = None


        self._emit(
            EventType.RUNTIME_STOPPED
        )



    # --------------------------------------------------
    # Execution
    # --------------------------------------------------

    def _run(
        self,
    ):

        while self._running:

            self.step()


            self._stop_event.wait(
                self.interval
            )



    def step(
        self,
    ):
        """
        Execute exactly one runtime cycle.

        Public for deterministic testing.
        """


        self.service_manager.tick_all()


        if self.cognitive_step:

            self.cognitive_step()


        self.tick_count += 1


        self.last_tick_time = datetime.now(
            UTC
        )