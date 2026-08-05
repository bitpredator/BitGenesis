from __future__ import annotations

from bitgenesis.knowledge.registry import KnowledgeRegistry


class CoreKnowledge:
    """
    Provides built-in knowledge available
    when BitGenesis is initialized.

    This represents innate knowledge,
    not learned knowledge.
    """


    def __init__(
        self,
        registry: KnowledgeRegistry,
    ):

        self.registry = registry



    def load(self) -> int:
        """
        Loads foundational entities.
        """


        entities = [

            {
                "name": "BitGenesis",

                "entity_type": "system",

                "attributes": {

                    "creator": "Bitpredator",

                    "type": (
                        "Artificial Cognitive Architecture"
                    ),

                    "purpose": (
                        "Create an artificial cognitive "
                        "system from scratch"
                    ),

                    "language": "Python",

                },
            },


            {
                "name": "Bitpredator",

                "entity_type": "person",

                "attributes": {

                    "role": (
                        "Creator of BitGenesis"
                    ),

                },
            },

        ]



        for entity in entities:

            self.registry.get_or_create(

                name=entity["name"],

                entity_type=entity["entity_type"],

                attributes=entity["attributes"],

            )



        return len(entities)