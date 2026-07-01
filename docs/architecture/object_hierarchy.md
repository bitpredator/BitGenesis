# Object Hierarchy

## Overview

BitGenesis is built around a small set of fundamental objects.

Every subsystem manipulates one or more of these objects instead of relying on loosely structured data.

This approach provides:

- consistency
- strong typing
- extensibility
- traceability
- serialization
- maintainability

The hierarchy defined in this document represents the conceptual object model of the BitGenesis architecture.

It is independent from any specific implementation.

---

# Root Object

Every object inside BitGenesis ultimately derives from a common conceptual base object.

```
BGObject
```

A `BGObject` provides the common behavior shared by every object in the system.

Typical responsibilities include:

- unique identification
- metadata
- timestamps
- serialization
- validation
- lifecycle tracking

---

# Core Hierarchy

The current conceptual hierarchy is defined as follows.

```
BGObject
│
├── Event
│
├── MemoryObject
│
├── KnowledgeObject
│
├── CognitiveObject
│   ├── Thought
│   ├── Decision
│   ├── Plan
│   └── Goal
│
├── PerceptionObject
│
├── RuntimeObject
│
└── ToolObject
```

This hierarchy is expected to evolve over time while preserving backward compatibility whenever possible.

---

# BGObject

The root object represents the minimum contract required by every component of the architecture.

Every object should provide:

- identity
- metadata
- serialization
- validation
- traceability

No subsystem-specific logic belongs to the root object.

---

# Event

Events describe facts.

They represent something that has already happened.

Events are immutable.

Every subsystem communicates through events whenever appropriate.

---

# MemoryObject

Represents information stored by the cognitive system.

Memory objects may exist in:

- Working Memory
- Short-Term Memory
- Long-Term Memory

Memory objects may evolve during their lifecycle.

---

# KnowledgeObject

Represents validated knowledge.

Unlike memory, knowledge is expected to be stable and reusable.

Knowledge objects may originate from:

- learning
- reasoning
- external sources

---

# CognitiveObject

Represents intermediate cognitive artifacts generated during thinking.

Examples include:

- thoughts
- decisions
- plans
- goals

These objects are typically temporary and exist only during reasoning processes.

---

# PerceptionObject

Represents interpreted sensory information.

Perception objects are generated before reasoning begins.

Their purpose is to transform raw input into structured cognitive information.

---

# RuntimeObject

Represents executable runtime entities.

Examples include:

- running tasks
- scheduled actions
- execution contexts

Runtime objects coordinate the execution phase of the architecture.

---

# ToolObject

Represents interactions with external systems.

Examples include:

- APIs
- file systems
- databases
- operating system resources

Tool objects isolate external dependencies from the cognitive core.

---

# Design Principles

The object hierarchy follows several architectural principles.

## Single Responsibility

Each object represents a single conceptual entity.

## Strong Separation

Objects belonging to different domains should not overlap in responsibility.

## Extensibility

New object types should extend existing abstractions whenever appropriate.

## Traceability

Every object should be identifiable throughout its lifecycle.

## Explainability

Objects should expose sufficient information to explain their role inside the cognitive process.

---

# Future Extensions

Future versions of BitGenesis may introduce additional object families, including:

- LearningObject
- LanguageObject
- NeuralObject
- SimulationObject

These additions should remain compatible with the existing conceptual hierarchy whenever possible.

---

# Architectural Notes

The hierarchy described in this document is conceptual.

Implementation details may vary across releases.

The conceptual model always takes precedence over implementation-specific optimizations.