from dataclasses import dataclass


@dataclass(slots=True)
class Intent:

    domain: str
    action: str
    target: str | None = None
    confidence: float = 1.0



class IntentDetector:
    """
    Detects user intentions from natural language.

    Supports:
    - English
    - Italian

    Current domains:
    - identity
    - memory
    - unknown
    """


    _IDENTITY_PATTERNS = {

        "creator": (

            # English

            "who created you",
            "who is your creator",
            "who made you",


            # Italian

            "chi ti ha creato",
            "chi ha creato te",
            "chi ha creato bitgenesis",
            "chi è il tuo creatore",
            "chi e il tuo creatore",
            "qual è il tuo creatore",
            "qual e il tuo creatore",
            "chi ti ha fatto",

        ),



        "name": (

            # English

            "who are you",
            "what is your name",
            "your name",


            # Italian

            "chi sei",
            "come ti chiami",
            "qual è il tuo nome",
            "qual e il tuo nome",

        ),



        "project": (

            # English

            "what is your project",
            "project name",


            # Italian

            "che progetto sei",
            "qual è il tuo progetto",
            "qual e il tuo progetto",

        ),



        "version": (

            # English

            "what is your version",
            "version",


            # Italian

            "qual è la tua versione",
            "qual e la tua versione",
            "che versione sei",

        ),



        "description": (

            # English

            "what are you",
            "describe yourself",
            "what do you do",


            # Italian

            "cosa sei",
            "descriviti",
            "cosa fai",
            "che cosa sei",

        ),
    }



    _MEMORY_QUERY_PATTERNS = {

        "latest": (

            "what is your latest memory",
            "what was your latest memory",


            "qual è il tuo ultimo ricordo",
            "qual e il tuo ultimo ricordo",

        ),



        "recent": (

            "show me your recent memories",
            "what do you remember",
            "tell me what you remember",


            "cosa ricordi",
            "cosa ti ricordi",
            "mostrami i tuoi ricordi",

        ),
    }



    def detect(
        self,
        text: str
    ) -> Intent | None:


        if not text:

            return None



        normalized = (
            text
            .strip()
            .lower()
        )



        if not normalized:

            return None



        # --------------------------
        # MEMORY SEARCH
        # --------------------------

        if "remember about" in normalized:


            target = normalized.split(
                "remember about",
                1
            )[1].strip()



            if target:

                return Intent(

                    domain="memory",

                    action="search",

                    target=target.rstrip("?"),

                    confidence=1.0,

                )



        if normalized.startswith(
            "do you remember "
        ):


            target = normalized.replace(
                "do you remember ",
                "",
                1,
            ).strip()



            if target:

                return Intent(

                    domain="memory",

                    action="search",

                    target=target.rstrip("?"),

                    confidence=1.0,

                )



        # --------------------------
        # MEMORY QUERY
        # --------------------------

        for target, patterns in self._MEMORY_QUERY_PATTERNS.items():

            for pattern in patterns:

                if pattern in normalized:

                    return Intent(

                        domain="memory",

                        action="query",

                        target=target,

                        confidence=1.0,

                    )



        # --------------------------
        # IDENTITY
        # --------------------------

        for target, patterns in self._IDENTITY_PATTERNS.items():

            for pattern in patterns:

                if pattern in normalized:

                    return Intent(

                        domain="identity",

                        action="query",

                        target=target,

                        confidence=1.0,

                    )



        # --------------------------
        # UNKNOWN
        # --------------------------

        return Intent(

            domain="unknown",

            action="unknown",

            target=text,

            confidence=0.0,

        )