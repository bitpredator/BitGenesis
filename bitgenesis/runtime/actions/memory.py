from bitgenesis.runtime.result import ActionResult

from bitgenesis.memory.object import MemoryObject



def store_memory(context) -> ActionResult:
    """
    Store a new memory object.
    """

    action_name = "store_memory"


    if context.memory_store is None:

        return ActionResult.fail(
            action=action_name,
            error="Memory store unavailable",
        )


    memory = MemoryObject(
        source="runtime",
        content=context.step.target,
    )


    context.memory_store.add(
        memory
    )


    return ActionResult.ok(
        action=action_name,
        data={
            "id": str(memory.id),
            "content": memory.content,
        },
        metadata={
            "status": "stored",
        },
    )



def retrieve_memory_items(context) -> ActionResult:
    """
    Retrieve stored memories.
    """

    action_name = "retrieve_memory"


    if context.memory_store is None:

        return ActionResult.fail(
            action=action_name,
            error="Memory store unavailable",
        )


    memories = context.memory_store.all()


    return ActionResult.ok(
        action=action_name,
        data={
            "items": memories,
            "count": len(memories),
        },
    )