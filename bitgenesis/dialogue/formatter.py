class ResponseFormatter:

    def format(self, intent, value):

        if intent is None:
            return None

        if value is None:
            return "I don't know."

        if intent.domain == "identity":

            return self._format_identity(
                intent.target,
                value,
            )

        return str(value)

    def _format_identity(self, target, value):

        templates = {
            "creator": "My creator is {}.",
            "name": "I am {}.",
            "project": "My project is {}.",
            "version": "I am currently running version {}.",
            "description": "{}",
        }

        template = templates.get(
            target,
            "{}",
        )

        return template.format(value)