from person import Person


class Employee(Person):
    def __init__(self, name="unknown", age=18, employee_id="123456", salary=25000):
        Person.__init__(self, name, age)
        self.employee_id = employee_id
        self.salary = salary

    def __str__(self):
        return Person.__str__(self) \
            + "\nEmployee ID: " + self.employee_id + " Salary : " + str(self.salary)

    def get_employee_id(self):
        return self.employee_id

    def get_salary(self):
        return self.salary