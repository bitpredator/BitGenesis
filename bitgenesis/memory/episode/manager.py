from bitgenesis.memory.episode.builder import EpisodeBuilder
from bitgenesis.memory.episode.segmenter import EpisodeSegmenter


class EpisodeManager:

    def __init__(self):

        self._episodes = []

        self._current = None

        self._builder = EpisodeBuilder()
        self._segmenter = EpisodeSegmenter()

    def add(self, memory):

        # Primo episodio
        if self._current is None:

            self._current = self._builder.build([memory])

            self._episodes.append(self._current)

            return self._current

        previous_memory = self._current.memories[-1]

        if self._segmenter.should_start_new_episode(
            previous_memory,
            memory,
        ):

            self._current = self._builder.build([memory])

            self._episodes.append(self._current)

            return self._current

        self._current.memories.append(memory)

        self._current.importance = max(
            m.importance
            for m in self._current.memories
        )

        self._current.title = (
            self._builder.generator.generate(
                self._current.memories
            )
        )

        return self._current

    def current(self):

        return self._current

    def all(self):

        return list(self._episodes)

    def count(self):

        return len(self._episodes)

    def clear(self):

        self._episodes.clear()

        self._current = None