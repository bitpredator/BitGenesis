# ADR 0004 — Persistent Memory Architecture

## Status

Accepted

---

## Context

BitGenesis already implements a structured memory subsystem capable of:

- storing memory objects
- retrieving information
- evaluating importance
- consolidating experiences
- generating episodes

Currently, memory exists primarily within the active runtime environment.

A cognitive architecture requires continuity beyond a single execution cycle.

Memory must survive system restarts and maintain long-term experience.

---

## Decision

Memory will evolve from runtime storage into a persistent cognitive subsystem.

The memory architecture will introduce:

- persistent storage backend
- serialization mechanisms
- restoration processes
- long-term memory management

Persistence will be implemented without coupling memory objects to storage mechanisms.

---

## Memory Separation Model

The architecture will maintain separation between:

### Memory Object

Represents cognitive information.

### Memory Store

Handles persistence and retrieval.

### Memory Engine

Handles processing and memory operations.

This preserves the domain model principles defined in ADR-0001.

---

## Design Constraints

### 1. Domain independence

Memory objects must not know how they are stored.

### 2. Backend flexibility

Storage implementation must be replaceable.

### 3. Explainable persistence

Memory lifecycle operations must remain observable.

---

## Consequences

### Positive

- Continuity between executions
- Foundation for long-term memory
- Improved cognitive realism
- Scalable storage architecture

### Negative

- Additional persistence layer
- Storage management complexity
- Requires migration strategy for future changes

---

## Future Work

This ADR enables:

- Persistent memory backend
- Memory restoration
- Long-term cognitive state
- Experience continuity

---

## Related Documents

- memory.md
- memory_object.md
- cognitive_object_model.md
- object_hierarchy.md