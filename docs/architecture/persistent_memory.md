```markdown
# Working Memory

> **The short-term cognitive processing subsystem of the BitGenesis architecture.**

---

# Overview

Working Memory represents the temporary cognitive space where BitGenesis processes information during an active cognitive cycle.

Unlike Persistent Memory, which stores long-term knowledge and experiences, Working Memory contains the information currently required for reasoning, planning and decision making.

Working Memory allows BitGenesis to maintain context while performing cognitive operations.

Without Working Memory, every cognitive process would operate only on isolated information without temporary context.

---

# Purpose

The Working Memory subsystem has several primary objectives:

- Maintain active cognitive context.
- Store temporary information during reasoning.
- Preserve relevant information during planning.
- Support decision making.
- Coordinate information between cognitive modules.
- Provide short-term state continuity during execution.

Working Memory represents the current mental state of the system.

---

# Design Philosophy

Working Memory is not a storage database.

It is an active cognitive workspace.

Information enters Working Memory because it is currently relevant.

Information leaves Working Memory when:

- the cognitive process completes;
- information becomes irrelevant;
- information is consolidated into long-term memory;
- context changes.

The purpose of Working Memory is not preservation.

The purpose is cognitive processing.

---

# Relationship With Other Memory Systems

BitGenesis separates memory into different cognitive layers.

```

```
             Cognitive Information

                    │

    ┌───────────────┴───────────────┐

    ▼                               ▼
```

Working Memory                  Persistent Memory

Short-term                      Long-term

Temporary                       Permanent

Active Context                  Stored Experience

```

Working Memory manages the present.

Persistent Memory manages the past.

---

# Position Inside the Cognitive Architecture

Working Memory operates between perception and reasoning.

```

Perception
│
▼
Working Memory
│
▼
Knowledge Retrieval
│
▼
Reasoning
│
▼
Planning
│
▼
Decision

```

Every active cognitive process should have access to the current Working Memory state.

---

# Responsibilities

Working Memory is responsible for:

- Maintaining active context.
- Holding temporary information.
- Tracking current objectives.
- Supporting reasoning sessions.
- Providing information to planners.
- Maintaining execution context.
- Tracking intermediate cognitive results.

Working Memory must not:

- Replace long-term memory.
- Permanently store experiences.
- Modify knowledge directly.
- Perform reasoning itself.

---

# Cognitive Context

The Working Memory state represents the current cognitive context.

A Working Memory instance may contain:

```

WorkingMemory

├── Current Input
├── Active Goal
├── Current Context
├── Retrieved Memories
├── Retrieved Knowledge
├── Reasoning State
├── Current Plan
├── Pending Actions
└── Execution Context

```

The content depends on the active cognitive process.

---

# Lifecycle

Working Memory follows the lifecycle of a cognitive operation.

```

Created
│
▼
Initialized
│
▼
Context Added
│
▼
Processing
│
▼
Updated
│
▼
Completed
│
▼
Cleared or Consolidated

```

A Working Memory instance exists only while it has cognitive relevance.

---

# Information Flow

Information enters Working Memory through several sources.

Examples:

- external perception;
- dialogue input;
- retrieved memories;
- knowledge queries;
- runtime events;
- previous reasoning results.

The information is then processed by cognitive components.

```

Input

↓

Working Memory

↓

Reasoning

↓

Decision

↓

Experience

↓

Learning

↓

Persistent Memory

```

---

# Attention and Working Memory

Future versions of BitGenesis will introduce an Attention System.

Attention will determine which information should enter Working Memory.

The relationship will be:

```

Information Sources

```
    │

    ▼
```

Attention System

```
    │

    ▼
```

Working Memory

```
    │

    ▼
```

Cognitive Processing

```

This prevents cognitive overload and allows prioritization of relevant information.

---

# Memory Consolidation

Working Memory is the entry point for future memory consolidation.

Not every temporary information becomes a permanent memory.

The consolidation process evaluates:

- importance;
- relevance;
- outcome;
- repetition;
- future usefulness.

```

Working Memory

```
    │

    ▼
```

Experience Evaluation

```
    │

    ▼
```

Memory Consolidation

```
    │

    ▼
```

Persistent Memory

```

---

# Future Evolution

Future versions of BitGenesis may extend Working Memory with:

- Attention integration.
- Context prioritization.
- Cognitive focus management.
- Memory decay mechanisms.
- Active information ranking.
- Parallel cognitive contexts.
- Multi-task processing.

---

# Architectural Requirements

Any future implementation of Working Memory must respect:

- clear separation from Persistent Memory;
- deterministic behaviour;
- explainable state transitions;
- modular interfaces;
- compatibility with the Cognitive Model.

Working Memory is the bridge between perception, memory and reasoning.

It represents the active cognitive space where BitGenesis processes the present.
```
