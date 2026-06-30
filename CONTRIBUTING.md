# Contributing to BitGenesis

Thank you for your interest in contributing to BitGenesis.

BitGenesis is an experimental cognitive architecture built from scratch.  
Because of its architectural nature, contributions are not treated as simple code changes, but as modifications to a structured system.

All contributions must follow strict engineering and documentation standards to ensure clarity, consistency, and long-term maintainability.

---

# 1. Core Philosophy

BitGenesis is built on the following principles:

- Every feature must be explainable.
- Every component must have a single responsibility.
- Every change must improve the system architecture, not just the code.
- Complexity is accepted only when it is necessary and justified.
- Behavior must remain predictable and testable.

---

# 2. Before You Start

Before writing any code, you must ensure:

- The change is aligned with the BitGenesis architecture.
- A clear technical motivation exists.
- The impact on other modules is understood.
- The change is not redundant with existing systems.

If a design decision is required, it MUST be documented through an Architecture Decision Record (ADR).

---

# 3. Architecture First Approach

BitGenesis follows an architecture-first development model.

This means:

1. Define the concept
2. Write the specification
3. Validate the design
4. Implement the code
5. Add tests
6. Update documentation

Code without design is not accepted.

---

# 4. Pull Request Rules

Every Pull Request must:

- Be small and focused on a single objective
- Include a clear description of the change
- Reference related issues or ADRs
- Include tests when applicable
- Include documentation updates when needed

Pull Requests that mix multiple unrelated changes will be rejected.

---

# 5. Code Standards

All contributions must follow these standards:

- Clear and meaningful naming
- Modular design (no monolithic components)
- No hidden side effects
- Explicit dependencies
- Deterministic behavior where possible

Code should be written for readability first, performance second.

---

# 6. Documentation Requirements

Every meaningful contribution must include:

- A description of the problem being solved
- The design decision behind the solution
- Any architectural implications
- Updated or new documentation if required

Undocumented changes are considered incomplete.

---

# 7. Testing Requirements

If your contribution includes logic or behavior changes:

- Unit tests must be included
- Edge cases must be considered
- Deterministic behavior should be verified when applicable

No untested logic will be accepted into the main branch.

---

# 8. Architecture Decision Records (ADR)

If your contribution introduces or modifies architecture-level decisions:

You must create or update an ADR inside:

docs/adr/

Each ADR must include:

- Context
- Decision
- Alternatives considered
- Consequences

---

# 9. Communication Style

When opening issues or pull requests:

- Be clear and precise
- Avoid vague descriptions
- Focus on technical reasoning
- Provide context when necessary

---

# 10. What Will NOT Be Accepted

The following types of contributions are not accepted:

- Unstructured or undocumented code
- Changes without clear motivation
- Large unreviewable pull requests
- Breaking architectural consistency without justification
- Duplicated or redundant implementations

---

# 11. Vision Alignment

All contributions must align with the long-term vision of BitGenesis:

> To build a modular, explainable and extensible cognitive architecture capable of learning, reasoning and evolving through structured components.

---

Thank you for contributing to BitGenesis.