from bitgenesis.memory.episode.object import Episode
from bitgenesis.memory.episode.title_generator import EpisodeTitleGenerator


class EpisodeBuilder:

    def __init__(self):

        self.generator = EpisodeTitleGenerator()

    def build(self, memories):

        episode = Episode()

        episode.memories.extend(memories)

        episode.title = self.generator.generate(memories)

        if memories:

            episode.importance = max(
                memory.importance
                for memory in memories
            )

        return episode