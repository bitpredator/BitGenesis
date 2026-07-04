def store_memory(step, executor):

    if executor.memory_store is not None:
        executor.memory_store.add(step.target)

    return {
        "action": step.action,
        "status": "stored",
    }


def retrieve_memory_items(step, executor):

    return {
        "action": step.action,
        "status": "retrieved",
        "data": step.target,
    }