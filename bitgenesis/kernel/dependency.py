from __future__ import annotations


class DependencyError(Exception):
    """
    Base dependency resolution error.
    """
    pass



class MissingDependencyError(
    DependencyError
):
    """
    Raised when a dependency cannot be resolved.
    """

    def __init__(
        self,
        dependency,
    ):

        super().__init__(
            f"Missing dependency: {dependency}"
        )



class CircularDependencyError(
    DependencyError
):
    """
    Raised when circular dependency detected.
    """

    def __init__(
        self,
        chain,
    ):

        super().__init__(
            "Circular dependency detected: "
            +
            " -> ".join(
                item.__name__
                for item in chain
            )
        )