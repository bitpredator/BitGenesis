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


    # ======================================================
    # System
    # ======================================================

    SYSTEM_STARTED = "system.started"
    SYSTEM_STOPPED = "system.stopped"



    # ======================================================
    # Kernel
    # ======================================================

    KERNEL_INITIALIZED = "kernel.initialized"
    KERNEL_SHUTDOWN = "kernel.shutdown"

    KERNEL_READY = "kernel.ready"



    # ======================================================
    # Services
    # ======================================================

    SERVICE_REGISTERED = "service.registered"
    SERVICE_UNREGISTERED = "service.unregistered"

    SERVICE_DISCOVERED = "service.discovered"

    SERVICE_STARTING = "service.starting"
    SERVICE_READY = "service.ready"
    SERVICE_STARTED = "service.started"

    SERVICE_STOPPING = "service.stopping"
    SERVICE_STOPPED = "service.stopped"

    SERVICE_FAILED = "service.failed"

    SERVICE_TICKED = "service.ticked"



    # ======================================================
    # Event Bus
    # ======================================================

    EVENT_PUBLISHED = "event.published"
    EVENT_DISPATCHED = "event.dispatched"
    EVENT_CONSUMED = "event.consumed"



    # ======================================================
    # Memory
    # ======================================================

    MEMORY_BOOTSTRAP = "memory.bootstrap"

    MEMORY_CREATED = "memory.created"
    MEMORY_UPDATED = "memory.updated"
    MEMORY_REMOVED = "memory.removed"

    MEMORY_RETRIEVED = "memory.retrieved"

    MEMORY_CONSOLIDATED = "memory.consolidated"



    # ======================================================
    # Identity
    # ======================================================

    IDENTITY_INITIALIZED = "identity.initialized"
    IDENTITY_UPDATED = "identity.updated"
    IDENTITY_LOADED = "identity.loaded"



    # ======================================================
    # Perception
    # ======================================================

    PERCEPTION_RECEIVED = "perception.received"
    PERCEPTION_PROCESSED = "perception.processed"



    # ======================================================
    # Cognitive Lifecycle
    # ======================================================

    COGNITIVE_RUNTIME_STARTED = (
        "cognition.runtime.started"
    )

    COGNITIVE_RUNTIME_STOPPED = (
        "cognition.runtime.stopped"
    )


    COGNITIVE_CYCLE_STARTED = (
        "cognition.cycle.started"
    )

    COGNITIVE_CYCLE_COMPLETED = (
        "cognition.cycle.completed"
    )

    COGNITIVE_CYCLE_FAILED = (
        "cognition.cycle.failed"
    )


    COGNITIVE_STAGE_STARTED = (
        "cognition.stage.started"
    )

    COGNITIVE_STAGE_COMPLETED = (
        "cognition.stage.completed"
    )



    # ======================================================
    # Reasoning
    # ======================================================

    REASONING_STARTED = "reasoning.started"
    REASONING_COMPLETED = "reasoning.completed"



    # ======================================================
    # Planning
    # ======================================================

    PLANNER_STARTED = "planning.started"
    PLANNER_COMPLETED = "planning.completed"
    PLANNER_FAILED = "planning.failed"


    # Compatibility with runtime/tests

    PLAN_CREATED = "planning.created"

    PLAN_STARTED = "planning.started"
    PLAN_COMPLETED = "planning.completed"
    PLAN_FAILED = "planning.failed"



    # ======================================================
    # Execution Plan
    # ======================================================

    EXECUTION_PLAN_CREATED = (
        "runtime.execution_plan.created"
    )

    EXECUTION_PLAN_STARTED = (
        "runtime.execution_plan.started"
    )

    EXECUTION_PLAN_COMPLETED = (
        "runtime.execution_plan.completed"
    )

    EXECUTION_PLAN_FAILED = (
        "runtime.execution_plan.failed"
    )



    # ======================================================
    # Learning
    # ======================================================

    LEARNING_STARTED = (
        "learning.started"
    )

    LEARNING_COMPLETED = (
        "learning.completed"
    )

    LEARNING_FAILED = (
        "learning.failed"
    )



    # ======================================================
    # Runtime
    # ======================================================

    RUNTIME_STARTED = "runtime.started"
    RUNTIME_STOPPED = "runtime.stopped"

    RUNTIME_TICKED = "runtime.ticked"



    # ======================================================
    # Execution Lifecycle
    # ======================================================

    EXECUTION_STARTED = (
        "runtime.execution.started"
    )

    EXECUTION_COMPLETED = (
        "runtime.execution.completed"
    )

    EXECUTION_FAILED = (
        "runtime.execution.failed"
    )



    # ======================================================
    # Action Lifecycle
    # ======================================================

    ACTION_STARTED = (
        "runtime.action.started"
    )

    ACTION_COMPLETED = (
        "runtime.action.completed"
    )

    ACTION_FAILED = (
        "runtime.action.failed"
    )



    # ======================================================
    # Step Lifecycle
    # ======================================================

    STEP_STARTED = (
        "runtime.step.started"
    )

    STEP_COMPLETED = (
        "runtime.step.completed"
    )

    STEP_FAILED = (
        "runtime.step.failed"
    )



    # ======================================================
    # Feedback Pipeline
    # ======================================================

    EXECUTION_FEEDBACK_CREATED = (
        "runtime.execution.feedback.created"
    )

    FEEDBACK_RECEIVED = (
        "runtime.feedback.received"
    )

    FEEDBACK_PROCESSED = (
        "runtime.feedback.processed"
    )



    # ======================================================
    # Legacy Compatibility
    # ======================================================

    TASK_STARTED = (
        "runtime.task_started"
    )

    TASK_COMPLETED = (
        "runtime.task_completed"
    )



    # ======================================================
    # Tooling
    # ======================================================

    TOOL_EXECUTED = (
        "tool.executed"
    )



    # ======================================================
    # Security
    # ======================================================

    SECURITY_ALERT = (
        "security.alert"
    )