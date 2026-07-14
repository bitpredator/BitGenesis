from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class ActionResult:
    """
    Result returned by runtime actions.
    """

    action: str

    success: bool

    data: Any = None

    error: str | None = None

    metadata: dict[str, Any] = field(
        default_factory=dict
    )


    @classmethod
    def ok(
        cls,
        action: str,
        data: Any = None,
        metadata: dict[str, Any] | None = None,
    ) -> "ActionResult":

        return cls(
            action=action,
            success=True,
            data=data,
            metadata=metadata or {},
        )


    @classmethod
    def fail(
        cls,
        action: str,
        error: str,
        metadata: dict[str, Any] | None = None,
    ) -> "ActionResult":

        return cls(
            action=action,
            success=False,
            error=error,
            metadata=metadata or {},
        )


    def __getitem__(
        self,
        key: str,
    ):

        """
        Backward compatibility with old runtime dictionaries.
        """

        if key == "action":
            return self.action

        if key == "success":
            return self.success

        if key == "error":
            return self.error

        if key in self.metadata:
            return self.metadata[key]

        if isinstance(self.data, dict):
            return self.data.get(key)

        raise KeyError(key)