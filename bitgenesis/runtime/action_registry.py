from __future__ import annotations

from typing import Type


class ActionRegistry:
    """
    Registry for runtime actions.

    Supports:
    - class based actions
    - function based actions
    - dynamic execution
    """


    def __init__(self):

        self._actions: dict[str, Type | callable] = {}


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


        # class based action
        if isinstance(action, type):

            return action()


        # function based action
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


        # object action
        if hasattr(action, "execute"):

            return action.execute(
                context
            )


        # function action
        if callable(action):

            return action(
                context
            )


        raise TypeError(
            f"Invalid action: {name}"
        )


    # --------------------------------------------------
    # Inspection
    # --------------------------------------------------

    def all(self):

        return tuple(
            self._actions.keys()
        )


    def clear(self):

        self._actions.clear()