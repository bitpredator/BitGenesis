# Cognition Subsystem Specification

## Overview

The Cognition subsystem represents the current mental state of BitGenesis.

Unlike the Memory subsystem, which stores past experiences, or the Reasoning subsystem, which evaluates information, Cognition maintains the live internal state of the artificial cognitive architecture.

It acts as the central representation of "what BitGenesis is thinking right now."

---

# Purpose

The purpose of the Cognition subsystem is to maintain a coherent, structured and continuously updated representation of the current cognitive state.

It provides the context required by higher-level cognitive processes without making decisions itself.

---

# Responsibilities

The Cognition subsystem is responsible for:

- Maintaining the current cognitive state.
- Tracking the active event.
- Tracking the current goal.
- Tracking the current task.
- Maintaining execution status.
- Managing the current attention focus.
- Providing contextual information to other subsystems.
- Ensuring state consistency.

---

# Non-Responsibilities

The Cognition subsystem does **not**:

- Perform reasoning.
- Store long-term memories.
- Execute actions.
- Plan future tasks.
- Communicate directly with external tools.
- Learn from experience.

These responsibilities belong to other subsystems.

---

# Internal Components

The subsystem consists of the following components.

## CognitiveState

Represents the complete internal state at a given moment.

## CognitiveContext

Builds the contextual information used by the Reasoning subsystem.

## CognitionManager

Controls every modification of the CognitiveState.

No subsystem should modify the state directly.

---

# State Lifecycle

The cognitive state evolves continuously.

Typical lifecycle:

```
Event Received

↓

State Updated

↓

Context Generated

↓

Reasoning

↓

Decision

↓

Planner

↓

Execution

↓

Memory Update

↓

State Updated
```

Every cognitive cycle produces a new internal state.

---

# Interactions

The Cognition subsystem interacts with:

| Subsystem | Purpose |
|-----------|----------|
| Kernel | Receives new events |
| Memory | Retrieves relevant memories |
| Reasoning | Provides contextual information |
| Planner | Shares current goals |
| Runtime | Receives execution updates |

---

# Data Model

The CognitiveState may contain:

- Current Event
- Current Goal
- Current Task
- Current Attention
- Active Plan
- Execution Status
- Active Memories
- Timestamp

Additional fields may be introduced in future versions.

---

# Design Principles

The Cognition subsystem follows these principles:

- Single Source of Truth
- Immutable Context Generation
- Controlled State Mutation
- Explainability
- Determinism
- Modularity

---

# Future Extensions

Future versions may introduce:

- Working Memory
- Attention Management
- Multi-Goal Handling
- Priority Scheduling
- Context Compression
- Self Monitoring
- Meta-Cognition

The current design intentionally leaves room for these future capabilities.

---

# Summary

The Cognition subsystem serves as the live representation of the internal mental state of BitGenesis.

It coordinates contextual information across the architecture while remaining independent from reasoning, planning and execution.