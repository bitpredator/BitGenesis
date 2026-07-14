from bitgenesis.memory.object import MemoryObject


def store_memory(context):

    if context.memory_store is None:

        return {
            "action": context.step.action,
            "status": "memory_unavailable",
        }


    memory = MemoryObject(
        source="runtime",
        content=context.step.target,
    )


    context.memory_store.add(
        memory
    )


    return {
        "action": context.step.action,
        "status": "stored",
        "memory_id": str(memory.id),
    }



def retrieve_memory_items(context):

    return {
        "action": context.step.action,
        "status": "retrieved",
        "data": context.step.target,
    }