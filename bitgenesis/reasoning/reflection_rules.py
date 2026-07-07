class ReflectionRules:

    def apply(self, facts):

        if not facts:
            return []

        reflections = []

        text = " ".join(
            str(fact).lower()
            for fact in facts
        )

        if all(
            language in text
            for language in (
                "python",
                "rust",
                "c++",
            )
        ):
            reflections.append(
                "The user enjoys programming languages."
            )

        if "planner" in text:
            reflections.append(
                "Planner subsystem is operational."
            )

        if (
            "memory" in text
            or "remember" in text
            or "recall" in text
        ):
            reflections.append(
                "Memory subsystem is functioning correctly."
            )

        return reflections