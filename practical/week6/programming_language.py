class ProgrammingLanguage:

    def __init__(self, name = "unknown", typing = "unknown", reflection = "unknown", year = "unknown"):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing == "Dynamic"

    def __str__(self):
        return "{}, {} Typing, Reflection = {}, first appeared in {}".format(self.name, self.typing, self.reflection, self.year)