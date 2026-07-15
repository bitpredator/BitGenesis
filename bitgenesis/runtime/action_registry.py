from __future__ import annotations

from typing import Type

from bitgenesis.events.event_bus import EventBus
from bitgenesis.events.event import Event
from bitgenesis.events.enums import (
    EventCategory,
    EventType,
)


class ActionRegistry:
    """
    Registry for runtime actions.

    Supports:
    - class based actions
    - function based actions
    - dynamic execution
    - action lifecycle events
    """

    def __init__(
        self,
        event_bus: EventBus | None = None,
    ):

        self._actions: dict[str, Type | callable] = {}

        self.event_bus = event_bus


    # --------------------------------------------------
    # Events
    # --------------------------------------------------

    def _emit(
        self,
        event_type,
        payload,
    ):

        if not self.event_bus:
            return


        self.event_bus.emit(
            Event(
                category=EventCategory.RUNTIME,
                type=event_type,
                source="action_registry",
                payload=payload,
            )
        )


    # --------------------------------------------------
    # Registration
    # --------------------------------------------------

    def register(
        self,
        name: str,
        action,
    ) -> None:

        self._actions[name] = action



    def unregister(
        self,
        name: str,
    ) -> None:

        self._actions.pop(
            name,
            None,
        )


    # --------------------------------------------------
    # Lookup
    # --------------------------------------------------

    def get(
        self,
        name: str,
    ):

        return self._actions.get(
            name
        )


    def contains(
        self,
        name: str,
    ) -> bool:

        return name in self._actions



    # --------------------------------------------------
    # Creation
    # --------------------------------------------------

    def create(
        self,
        name: str,
    ):

        action = self.get(name)

        if action is None:
            return None


        if isinstance(action, type):

            return action()


        return action



    # --------------------------------------------------
    # Execution
    # --------------------------------------------------

    def execute(
        self,
        name: str,
        context,
    ):


        action = self.create(name)


        if action is None:

            raise ValueError(
                f"Unknown action: {name}"
            )


        self._emit(
            EventType.ACTION_STARTED,
            {
                "action": name,
            },
        )


        try:

            if hasattr(action, "execute"):

                result = action.execute(
                    context
                )


            elif callable(action):

                result = action(
                    context
                )


            else:

                raise TypeError(
                    f"Invalid action: {name}"
                )


        except Exception as exc:

            self._emit(
                EventType.ACTION_FAILED,
                {
                    "action": name,
                    "error": str(exc),
                },
            )

            raise



        self._emit(
            EventType.ACTION_COMPLETED,
            {
                "action": name,
            },
        )


        return result



    # --------------------------------------------------
    # Inspection
    # --------------------------------------------------

    def all(self):

        return tuple(
            self._actions.keys()
        )



    def clear(self):

        self._actions.clear()