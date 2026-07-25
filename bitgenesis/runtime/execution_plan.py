from __future__ import annotations

from dataclasses import dataclass, field
from uuid import uuid4

from bitgenesis.runtime.execution_step import ExecutionStep


@dataclass
class ExecutionPlan:


    id: str = field(
        default_factory=lambda: str(uuid4())
    )


    steps: list[ExecutionStep] = field(
        default_factory=list
    )


    def add(
        self,
        step: ExecutionStep,
    ):

        self.steps.append(
            step
        )


    def ordered_steps(
        self,
    ):

        return sorted(
            self.steps,
            key=lambda step: step.priority,
        )


    def empty(
        self,
    ):

        return not bool(
            self.steps
        )