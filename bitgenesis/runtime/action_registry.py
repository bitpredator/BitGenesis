class ActionRegistry:

    def __init__(self):

        self._actions = {}

    def register(self, name, handler):

        self._actions[name] = handler

    def execute(self, name, step, executor):

        handler = self._actions.get(name)

        if handler is None:

            return {
                "action": name,
                "status": "unknown_action"
            }

        return handler(step, executor)