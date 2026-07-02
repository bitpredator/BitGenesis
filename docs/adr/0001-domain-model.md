# ADR 0001 — Domain Model Architecture

## Status

Accepted

---

## Context

BitGenesis is designed as a cognitive architecture rather than a traditional software system.

The system requires a clear and consistent model to represent:

- core identity objects
- cognitive entities
- memory and experience representation
- system-wide event communication

Without a strict domain model, the architecture would quickly become inconsistent, especially as more cognitive subsystems (Memory, Reasoning, Planning, Learning) are introduced.

---

## Decision

We introduce a layered domain model composed of three primary abstractions:

### 1. Entity (Root Level)

`Entity` is the base abstraction of all objects in the system.

It provides:

- unique identifier
- creation timestamp
- update timestamp
- mutation tracking via `touch()`

Entity has no cognitive meaning.

It only defines existence.

---

### 2. CognitiveObject (Cognitive Layer)

`CognitiveObject` extends `Entity` and introduces cognitive properties:

- metadata
- importance
- confidence
- tags

It represents any object that participates in cognitive processing but is not yet specialized.

This layer ensures that all cognitive structures share a consistent interface.

---

### 3. Domain-Specific Cognitive Objects

Specialized objects inherit from `CognitiveObject`.

Example:

#### MemoryObject

Represents a stored experience.

It introduces:

- source (origin of the memory)
- content (stored information)
- links (relationships with other memories)

MemoryObject does NOT contain logic for storage, retrieval, or processing.

It is a pure domain representation.

---

## Event-Driven Communication

All interactions between subsystems are designed to go through an Event System.

This ensures:

- loose coupling between components
- traceable system behavior
- extensibility for future cognitive modules

---

## Design Constraints

The following constraints are enforced across the domain model:

### 1. Keyword-only initialization

All dataclasses use:

```python
@dataclass(slots=True, kw_only=True)

This ensures:

- explicit object construction
- improved readability
- prevention of positional argument ambiguity in inheritance chains

2. Separation of concerns

Domain objects:

- DO NOT persist themselves
- DO NOT execute business logic
- DO NOT manage system state

They only represent structure and meaning.

3. Immutability of meaning

While objects may mutate structurally (e.g. tags, links), their semantic role remains stable.

Example:

A MemoryObject remains a MemoryObject throughout its lifecycle.

Consequences
Positive
- Clear separation between data and behavior
- Scalable cognitive architecture
- Easy extension for future cognitive layers (Knowledge, Reasoning, Planning)
- Predictable object hierarchy

Negative
- Requires additional service layers (Store, Engine, Manager)
- Slight increase in initial complexity

Future Work

This ADR sets the foundation for:

- MemoryStore (next component)
- MemoryEngine
- Knowledge system
- Reasoning layer
- Planning system

Each subsystem will follow the same architectural principles.

- Related Documents
- object_hierarchy.md
- cognitive_object_model.md
- core_data_model.md
- events.md
