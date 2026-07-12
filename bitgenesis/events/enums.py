"""
Event-related enumerations.

This module defines the core vocabulary used by the BitGenesis Event System.
"""

from enum import Enum


class EventCategory(Enum):
    """
    High-level domain that generated the event.
    """

    SYSTEM = "system"
    KERNEL = "kernel"
    COGNITION = "cognition"
    PERCEPTION = "perception"
    REASONING = "reasoning"
    PLANNING = "planning"
    MEMORY = "memory"
    IDENTITY = "identity"
    KNOWLEDGE = "knowledge"
    LEARNING = "learning"
    LANGUAGE = "language"
    RUNTIME = "runtime"
    TOOL = "tool"
    SECURITY = "security"


class EventPriority(Enum):
    """
    Event scheduling priority.
    """

    LOW = 10
    NORMAL = 20
    HIGH = 30
    CRITICAL = 40


class EventType(Enum):
    """
    Specific event that occurred inside the system.
    """

    #
    # System
    #
    SYSTEM_STARTED = "system.started"
    SYSTEM_STOPPED = "system.stopped"

    #
    # Kernel
    #
    KERNEL_INITIALIZED = "kernel.initialized"
    KERNEL_SHUTDOWN = "kernel.shutdown"

    #
    # Event Bus
    #
    EVENT_PUBLISHED = "event.published"
    EVENT_DISPATCHED = "event.dispatched"
    EVENT_CONSUMED = "event.consumed"

    #
    # Memory
    #
    MEMORY_CREATED = "memory.created"
    MEMORY_UPDATED = "memory.updated"
    MEMORY_REMOVED = "memory.removed"
    
    #
    # Identity
    #
    IDENTITY_INITIALIZED = "identity.initialized"
    IDENTITY_UPDATED = "identity.updated"
    IDENTITY_LOADED = "identity.loaded"

    #
    # Perception
    #
    PERCEPTION_RECEIVED = "perception.received"
    PERCEPTION_PROCESSED = "perception.processed"

    #
    # Reasoning
    #
    REASONING_STARTED = "reasoning.started"
    REASONING_COMPLETED = "reasoning.completed"

    #
    # Planning
    #
    PLAN_CREATED = "planning.created"
    PLAN_COMPLETED = "planning.completed"

    #
    # Learning
    #
    LEARNING_STARTED = "learning.started"
    LEARNING_COMPLETED = "learning.completed"

    #
    # Runtime
    #
    TASK_STARTED = "runtime.task_started"
    TASK_COMPLETED = "runtime.task_completed"

    #
    # Tooling
    #
    TOOL_EXECUTED = "tool.executed"

    #
    # Security
    #
    SECURITY_ALERT = "security.alert"