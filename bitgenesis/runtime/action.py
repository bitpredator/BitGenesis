from __future__ import annotations

from abc import ABC, abstractmethod

from bitgenesis.runtime.action_context import ActionContext
from bitgenesis.runtime.result import ActionResult


class RuntimeAction(ABC):
    """
    Base class for executable runtime actions.

    Runtime actions are atomic executable capabilities
    exposed through the BitGenesis runtime layer.

    Lifecycle:

    ActionRegistry
        ↓
    RuntimeExecutor
        ↓
    RuntimeAction.execute()
        ↓
    ActionResult
    """


    name: str | None = None


    def __init_subclass__(cls, **kwargs):
        """
        Validate action definition.
        """

        super().__init_subclass__(**kwargs)

        if not cls.name:
            raise TypeError(
                f"RuntimeAction {cls.__name__} must define a name"
            )


    @abstractmethod
    def execute(
        self,
        context: ActionContext,
    ) -> ActionResult:
        """
        Execute the action.

        Args:
            context:
                Runtime execution context.

        Returns:
            ActionResult describing execution outcome.
        """

        raise NotImplementedError