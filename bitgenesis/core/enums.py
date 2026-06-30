"""
Shared enumerations.
"""

from enum import Enum


class Status(Enum):
    CREATED = "created"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"