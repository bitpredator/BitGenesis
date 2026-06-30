# BitGenesis Architecture Glossary

## Purpose

This glossary defines the official terminology used throughout the BitGenesis project.

Every specification, document and implementation should use these terms consistently.

---

# Artificial Cognitive Architecture

A modular software architecture designed to simulate cognitive processes through independent and cooperating subsystems.

---

# Cognition

The subsystem responsible for maintaining the current internal mental state.

---

# Cognitive State

The complete representation of the current internal status of BitGenesis.

It reflects what the system is processing at a specific moment.

---

# Cognitive Context

A structured collection of information supplied to the Reasoning subsystem.

It combines:

- Current State
- Relevant Memory
- Active Goals
- Current Event

---

# Event

A structured message representing something that happened inside or outside the system.

Events are the primary communication mechanism between subsystems.

---

# Kernel

The central coordinator responsible for routing events across the architecture.

The Kernel never performs reasoning.

---

# Memory

The subsystem responsible for storing and retrieving experiences.

Memory represents the past.

---

# Knowledge

Structured information extracted from accumulated memories.

Knowledge represents long-term understanding.

---

# Reasoning

The subsystem responsible for evaluating information and producing decisions.

Reasoning never executes actions.

---

# Decision

The output produced by the Reasoning subsystem after evaluating the available context.

---

# Planner

The subsystem responsible for converting decisions into executable plans.

---

# Plan

An ordered sequence of actions required to achieve a goal.

---

# Runtime

The subsystem responsible for executing plans.

---

# Tool

Any external software or service that BitGenesis can interact with.

Examples include:

- File System
- Git
- GitHub
- REST APIs
- Databases

---

# Attention

The mechanism determining which information currently receives processing priority.

Future subsystem.

---

# Working Memory

Temporary information actively used during reasoning.

Future subsystem.

---

# Long-Term Memory

Persistent storage of experiences and knowledge.

---

# Goal

A desired future state that the Planner attempts to achieve.

---

# Task

A concrete unit of work executed as part of a plan.

---

# Execution

The process of carrying out a generated plan.

---

# Learning

The subsystem responsible for improving future behavior through accumulated experience.

---

# Explainability

The capability of describing how and why a decision was made.

This is one of the core principles of BitGenesis.

---

# Determinism

The property that identical inputs should produce identical outputs whenever possible.

---

# Modularity

The architectural principle that every subsystem has a single responsibility and can evolve independently.

---

# Event-Driven Architecture

An architectural style where subsystems communicate through events instead of direct coupling.

---

# Subsystem

A major architectural module responsible for a specific cognitive capability.

Examples:

- Memory
- Reasoning
- Planner
- Runtime

---

# Component

An internal implementation element belonging to a subsystem.

Example:

The Memory subsystem may contain multiple components such as stores, indexes and listeners.