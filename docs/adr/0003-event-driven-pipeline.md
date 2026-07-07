# ADR 0003 — Event Driven Cognitive Pipeline

## Status

Accepted

---

## Context

BitGenesis is composed of multiple independent cognitive subsystems.

Direct communication between modules would create strong dependencies and make future architectural evolution difficult.

The project already contains an Event System designed to provide communication between components.

A consistent communication model is required as the number of cognitive modules increases.

---

## Decision

All major subsystem communication will use an event-driven architecture.

Events represent meaningful transitions or information exchanges inside the cognitive system.

Examples:

- memory creation
- memory retrieval
- reasoning request
- reasoning result
- action request
- action completion

---

## Event Responsibilities

Events are responsible for:

- describing system changes
- transporting structured information
- enabling subsystem notification
- maintaining execution traceability

Events are not responsible for:

- executing business logic
- storing permanent state
- replacing domain objects

---

## Design Constraints

### 1. Loose coupling

Subsystems should depend on event contracts rather than concrete implementations.

### 2. Traceability

Important cognitive transitions should be observable through emitted events.

### 3. Extensibility

New modules should integrate by subscribing to existing events or introducing new event types.

---

## Consequences

### Positive

- Improved modularity
- Better debugging capability
- Easier future expansion
- Reduced subsystem dependency

### Negative

- More complex execution flow
- Requires event contract management
- Debugging asynchronous flows may require additional tooling

---

## Future Work

This ADR enables:

- Complete cognitive event pipeline
- Runtime observability
- Event history tracking
- Advanced subsystem coordination

---

## Related Documents

- events.md
- event_bus.py
- dispatcher.py
- cognitive_pipeline.md