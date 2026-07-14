from __future__ import annotations

from abc import ABC, abstractmethod

from bitgenesis.runtime.action_context import ActionContext
from bitgenesis.runtime.result import ActionResult


class RuntimeAction(ABC):
    """
    Base class for executable runtime actions.

    An action represents an operation that can be executed
    by the BitGenesis runtime.

    Actions are resolved by the ActionRegistry and executed
    by the RuntimeExecutor.
    """


    name: str = ""


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