def query_knowledge_graph(context):

    if context.graph is None:

        return {
            "action": context.step.action,
            "status": "graph_unavailable",
        }

    return {
        "action": context.step.action,
        "status": "queried",
        "data": context.step.target,
    }