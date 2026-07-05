from bitgenesis.reasoning.intent_detector import Intent


class ResponseFormatter:

    def format(self, resolution):

        if resolution is None:
            return None

        if not resolution.success:
            return "I don't know."

        if resolution.domain == "identity":

            return self._format_identity(
                resolution.target,
                resolution.value,
            )

        return str(resolution.value)

    def _format_identity(self, target, value):

        templates = {
            "creator": "My creator is {}.",
            "name": "I am {}.",
            "project": "My project is {}.",
            "version": "I am currently running version {}.",
            "description": "{}",
        }

        template = templates.get(target, "{}")

        return template.format(value)