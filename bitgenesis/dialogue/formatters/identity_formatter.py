from bitgenesis.reasoning.resolution import Resolution

class IdentityFormatter:

    def format(self, resolution: Resolution):

        value = resolution.value

        if value is None:
            return "I don't know."

        match resolution.target:

            case "creator":
                return f"My creator is {value}."

            case "name":
                return f"I am {value}."

            case "project":
                return f"My project is {value}."

            case "version":
                return f"I am currently running version {value}."

            case "description":
                return str(value)

            case _:
                return str(value)