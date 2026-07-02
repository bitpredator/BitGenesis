# Memory Object Specification

## Purpose

The MemoryObject represents an experience acquired by the BitGenesis cognitive system.

It is the fundamental unit of episodic memory and serves as the primary source of information for reasoning, learning, planning, and long-term knowledge formation.

A MemoryObject stores observations, interactions, or internal events together with contextual information that allows the system to recall and interpret past experiences.

---

# Responsibilities

A MemoryObject is responsible for:

- Representing a single remembered experience.
- Preserving contextual information.
- Tracking its own lifecycle.
- Maintaining relationships with other memories.
- Providing metadata useful for reasoning and learning.

A MemoryObject is **not** responsible for:

- Making decisions.
- Executing actions.
- Performing reasoning.
- Managing persistence.
- Updating itself autonomously.

---

# Design Principles

Every MemoryObject must satisfy the following principles:

- Represents exactly one experience.
- Has a globally unique identifier.
- Is explainable.
- Is serializable.
- Can be linked to other MemoryObjects.
- Can evolve through metadata updates.
- Is independent from storage technologies.

---

# Core Attributes

Every MemoryObject must expose the following attributes.

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| id | UUID | Yes | Globally unique identifier |
| created_at | datetime | Yes | Creation timestamp |
| updated_at | datetime | Yes | Last modification timestamp |
| source | str | Yes | Origin of the memory |
| content | Any | Yes | Remembered information |
| metadata | dict | Yes | Additional structured information |
| importance | float | Yes | Relative importance score |
| confidence | float | Yes | Confidence in stored information |
| tags | list[str] | No | Search tags |
| links | list[str] | No | Related MemoryObject identifiers |

---

# Lifecycle

```
Created
    │
    ▼
Stored
    │
    ▼
Updated
    │
    ├── Archived
    └── Deleted
```

---

# Relationships

A MemoryObject may be connected to:

- Perception
- Event
- KnowledgeObject
- Thought
- Decision

These relationships are logical rather than physical.

---

# Constraints

A valid MemoryObject must satisfy the following constraints.

- Identifier cannot change.
- Creation timestamp cannot change.
- Importance must be between 0.0 and 1.0.
- Confidence must be between 0.0 and 1.0.
- Metadata keys must be unique.
- Tags should be unique.
- Circular links should be avoided.

---

# Usage

MemoryObjects may be created by:

- Memory Engine
- Learning Engine
- Perception System

MemoryObjects may be consumed by:

- Reasoning Engine
- Planner
- Learning Engine
- Knowledge Engine

---

# Future Extensions

Future versions may introduce:

- Emotional weight
- Decay score
- Recall frequency
- Embeddings
- Semantic clusters
- Temporal relationships
- Spatial relationships

These extensions must remain backward compatible.

---

# Related Documents

- memory.md
- cognitive_object_model.md
- object_specification.md
- core_data_model.md