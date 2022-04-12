from person import Person


class Musician(Person):
    def __init__(self, name="unknown", age=18, equipment=""):
        Person.__init__(self, name, age)
        #super().__init__(name, age)
        self.equipment = equipment

    def __str__(self):
        return Person.__str__(self) + "\nEquipment : " + self.equipment

    def get_equipment(self):
        return self.equipment

