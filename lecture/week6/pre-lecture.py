
products = [["phone", 340, False], ["PC", 1420.95, True], ["Plant", 24.5, True]]

# on_sale_products = ?

for i in range(0, len(products)):
    if products[i][2] == True:
        print(products[i])










class Person(object):
    def __init__(self, name = "unknown", number_of_tacos = "unknown", left_taco = 5):
        self.name = name
        self.number_of_tacos = number_of_tacos
        self.left_taco = left_taco
        
        left_taco = 5 - number_of_tacos


    def __str__(self):
        return "{}, {}points, {}tacos left".format(self.name, self.number_of_tacos, self.left_taco)

p1 = Person("Ben", 2)
print(p1)
