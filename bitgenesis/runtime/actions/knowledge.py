def query_knowledge_graph(step, executor):

    if executor.graph is None:
        return {
            "action": step.action,
            "status": "graph_unavailable",
        }

    return {
        "action": step.action,
        "status": "queried",
        "data": step.target,
    }