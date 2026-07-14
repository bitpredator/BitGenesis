from bitgenesis.runtime.result import ActionResult



def query_knowledge_graph(context):

    if context.graph is None:

        return ActionResult.fail(
            action=context.step.action,
            error="Knowledge graph unavailable",
        )


    return ActionResult.ok(
        action=context.step.action,
        data={
            "status": "queried",
            "target": context.step.target,
        },
    )