from bitgenesis.knowledge.relation_mapper import RelationMapper


def test_creator_relation():

    assert RelationMapper.relation_for("creator") == "creator_of"


def test_author_relation():

    assert RelationMapper.relation_for("author") == "author_of"


def test_developer_relation():

    assert RelationMapper.relation_for("developer") == "developer_of"


def test_language_relation():

    assert RelationMapper.relation_for("language") == "written_in"


def test_company_relation():

    assert RelationMapper.relation_for("company") == "owned_by"


def test_case_insensitive():

    assert RelationMapper.relation_for("Creator") == "creator_of"
    assert RelationMapper.relation_for("CREATOR") == "creator_of"


def test_unknown_relation():

    assert RelationMapper.relation_for("pizza") == "related_to"


def test_none_relation():

    assert RelationMapper.relation_for(None) == "related_to"