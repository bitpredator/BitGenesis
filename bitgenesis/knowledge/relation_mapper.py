class RelationMapper:

    RELATIONS = {
        "creator": "creator_of",
        "author": "author_of",
        "developer": "developer_of",
        "project": "project",
        "language": "written_in",
        "company": "owned_by",
        "organization": "member_of",
        "owner": "owned_by",
        "server": "hosted_on",
        "host": "hosted_on",
    }

    @classmethod
    def relation_for(cls, key: str) -> str:

        if key is None:
            return "related_to"

        return cls.RELATIONS.get(
            key.strip().lower(),
            "related_to",
        )