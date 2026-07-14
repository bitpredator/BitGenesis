from __future__ import annotations

from bitgenesis.runtime.action_registry import ActionRegistry

from bitgenesis.runtime.actions.memory import (
    store_memory,
    retrieve_memory_items,
)

from bitgenesis.runtime.actions.knowledge import (
    query_knowledge_graph,
)


def register_default_actions(
    registry: ActionRegistry,
) -> None:
    """
    Register built-in runtime actions.

    This is the default action set shipped with BitGenesis.

    Future action providers can extend this registry without
    modifying the executor.
    """

    # Memory actions

    registry.register(
        "store_memory",
        store_memory,
    )

    registry.register(
        "retrieve_memory_items",
        retrieve_memory_items,
    )


    # Knowledge actions

    registry.register(
        "query_knowledge_graph",
        query_knowledge_graph,
    )