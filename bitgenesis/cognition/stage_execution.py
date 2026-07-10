from dataclasses import dataclass, field
from datetime import datetime, UTC


@dataclass(slots=True)
class StageExecution:
    """
    Metadata about a cognitive stage execution.
    """

    stage: str

    started_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    completed_at: datetime | None = None

    success: bool = False

    error: str | None = None

    def complete(self):
        self.completed_at = datetime.now(UTC)
        self.success = True

    def fail(self, error: Exception):
        self.completed_at = datetime.now(UTC)
        self.error = str(error)