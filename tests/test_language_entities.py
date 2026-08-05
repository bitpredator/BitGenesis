from bitgenesis.language.entity import (
    EntityType,
)

from bitgenesis.language.entity_extractor import (
    EntityExtractor,
)

from bitgenesis.language.processor import (
    LanguageProcessor,
)



def test_entity_extractor_project():

    extractor = EntityExtractor()


    entities = extractor.extract(
        "Chi ha creato BitGenesis?"
    )


    assert len(entities) == 1


    entity = entities[0]


    assert entity.type == EntityType.PROJECT

    assert entity.value == "bitgenesis"



def test_entity_extractor_services():

    extractor = EntityExtractor()


    entities = extractor.extract(
        "Uso Python e GitHub per sviluppare"
    )


    values = {
        entity.value
        for entity in entities
    }


    assert "python" in values

    assert "github" in values



def test_entity_extractor_language():

    extractor = EntityExtractor()


    entities = extractor.extract(
        "Rispondi in italiano"
    )


    assert any(
        entity.type == EntityType.LANGUAGE
        for entity in entities
    )



def test_entity_extractor_memory():

    extractor = EntityExtractor()


    entities = extractor.extract(
        "Salva questa informazione nella memoria"
    )


    assert any(
        entity.type == EntityType.MEMORY
        for entity in entities
    )



def test_entity_extractor_no_duplicates():

    extractor = EntityExtractor()


    entities = extractor.extract(
        "BitGenesis BitGenesis"
    )


    projects = [
        entity
        for entity in entities
        if entity.type == EntityType.PROJECT
    ]


    assert len(projects) == 1



def test_processor_returns_entities():

    processor = LanguageProcessor()


    context = processor.process(
        "Chi ha creato BitGenesis?"
    )


    assert context.entities


    assert any(
        entity.type == EntityType.PROJECT
        for entity in context.entities
    )



def test_language_context_serializes_entities():

    processor = LanguageProcessor()


    context = processor.process(
        "Uso Python con BitGenesis"
    )


    data = context.to_dict()


    assert "entities" in data


    assert isinstance(
        data["entities"],
        list,
    )


    assert len(
        data["entities"]
    ) > 0