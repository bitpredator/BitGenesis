# ADR 0005 — Cognitive Runtime Location

## Status

Accepted

---

## Context

BitGenesis is evolving from a collection of independent cognitive modules into a coordinated cognitive architecture.

The system already contains several execution-related components:

- Kernel layer
- Cognition layer
- Execution Runtime
- Cognitive modules

As the architecture grows, a clear separation is required between:

- system initialization
- cognitive coordination
- action execution

Without a defined location for the Cognitive Runtime, responsibilities may become mixed between Kernel, Brain, and Runtime components.

This could lead to:

- excessive coupling
- unclear ownership of cognitive processes
- difficulty extending future cognitive capabilities

---

## Decision

The Cognitive Runtime will be located inside the `cognition` package.

The new component will be:

bitgenesis/cognition/cognitive_runtime.py


The Cognitive Runtime becomes the coordinator of cognitive processing.

---

## Responsibilities

The Cognitive Runtime is responsible for:

- managing cognitive execution flow
- coordinating cognitive subsystems
- controlling cognitive pipeline progression
- maintaining cognitive processing state
- communicating through the Event System

The Cognitive Runtime does NOT:

- store memories directly
- execute external actions directly
- contain domain objects
- replace specialized cognitive modules

---

# Architectural Separation

## Kernel

Location:

bitgenesis/kernel/


Responsibility:

- system initialization
- dependency configuration
- component creation
- lifecycle management

The Kernel starts the Cognitive Runtime but does not control cognitive decisions.

---

## Cognitive Runtime

Location:

bitgenesis/cognition/


Responsibility:

- cognitive orchestration
- pipeline coordination
- cognitive state transitions
- subsystem communication

---

## Execution Runtime

Location:

bitgenesis/runtime/


Responsibility:

- action execution
- tool interaction
- external operations

The Execution Runtime receives approved actions from the cognitive system.

---

# Resulting Architecture

             Kernel
                |
                v

      Cognitive Runtime
                |
  +-------------+-------------+
  |             |             |
  v             v             v

Perception Memory Reasoning

                |
                v

           Planning

                |
                v

      Execution Runtime

                |
                v

             Tools


---

# Design Constraints

The following rules are established:

## 1. No Cognitive Logic in Kernel

The Kernel must never contain:

- reasoning rules
- memory decisions
- planning logic

---

## 2. No Cognitive Coordination in Execution Runtime

The Execution Runtime only performs actions.

It does not decide:

- what should happen
- why it should happen
- whether an action is appropriate

---

## 3. Cognitive Runtime Uses Events

Communication between cognitive components must use the Event System.

Direct dependencies between unrelated modules should be avoided.

---

# Consequences

## Positive

- Clear architectural boundaries
- Better modularity
- Easier subsystem replacement
- Improved explainability
- Supports future autonomous cognitive cycles

---

## Negative

- Additional abstraction layer
- More explicit coordination logic required
- Increased initial implementation complexity

---

# Future Work

This ADR enables the creation of:

- `cognitive_runtime.py`
- cognitive pipeline executor
- cognitive cycle management
- runtime state tracking
- adaptive cognitive loops

---

# Related Documents

- 0002-cognitive-runtime.md
- 0003-event-driven-pipeline.md
- cognitive_runtime.md
- cognitive_pipeline.md
- system_layers.md

