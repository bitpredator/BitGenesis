class EpisodeSegmenter:

    def should_start_new_episode(
        self,
        previous_memory,
        current_memory,
    ) -> bool:

        # Prima memoria in assoluto
        if previous_memory is None:
            return True

        previous_category = (
            previous_memory.content
            .get("event", {})
            .get("category")
        )

        current_category = (
            current_memory.content
            .get("event", {})
            .get("category")
        )

        # Cambio categoria → nuovo episodio
        if previous_category != current_category:
            return True

        # Altrimenti continua l'episodio corrente
        return False