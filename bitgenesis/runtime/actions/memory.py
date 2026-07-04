def store_memory(context):

    if context.memory_store is not None:
        context.memory_store.add(context.step.target)

    return {
        "action": context.step.action,
        "status": "stored",
    }


def retrieve_memory_items(context):

    return {
        "action": context.step.action,
        "status": "retrieved",
        "data": context.step.target,
    }