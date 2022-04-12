class Person(object):
    def __init__(self, name="Unknown", age=18):
        self.name = name
        self.age = age

    def __str__(self):
        return "{} {}".format(self.name, self.age)

    def __repr__(self):
        return "{} {}".format(self.name, self.age)
