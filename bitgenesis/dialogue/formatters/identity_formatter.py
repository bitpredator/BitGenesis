from __future__ import annotations


from bitgenesis.reasoning.resolution import Resolution
from bitgenesis.language.detector import Language



class IdentityFormatter:
    """
    Formats identity related responses.

    Supports multilingual responses based on the detected
    input language.

    Default language remains English for backwards compatibility.
    """


    def format(
        self,
        resolution: Resolution,
        language: Language | None = None,
    ):


        value = resolution.value


        if value is None:

            if language == Language.ITALIAN:

                return "Non lo so."

            return "I don't know."



        italian = (
            language == Language.ITALIAN
        )



        match resolution.target:


            case "creator":

                if italian:

                    return (
                        f"Il mio creatore è {value}."
                    )

                return (
                    f"My creator is {value}."
                )



            case "name":

                if italian:

                    return (
                        f"Sono {value}."
                    )

                return (
                    f"I am {value}."
                )



            case "project":

                if italian:

                    return (
                        f"Il mio progetto è {value}."
                    )

                return (
                    f"My project is {value}."
                )



            case "version":

                if italian:

                    return (
                        f"Sto eseguendo la versione {value}."
                    )

                return (
                    f"I am currently running version {value}."
                )



            case "description":

                return str(value)



            case _:

                return str(value)