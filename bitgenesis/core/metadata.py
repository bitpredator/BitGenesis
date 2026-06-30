"""
Shared metadata model for all Core Objects.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime


@dataclass(frozen=True, slots=True)
class Metadata:
    """
    Common metadata shared by every Core Object.
    """

    timestamp: datetime = field(default_factory=lambda: datetime.now(UTC))
    schema_version: int = 1