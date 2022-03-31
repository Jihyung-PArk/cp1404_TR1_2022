class User(object):
    def __init__(self, name = "unknown", num_of_tacos = 5, score = 0):
        self.name = name
        self.num_of_tacos = num_of_tacos
        self.score = score
        
    def give_a_taco(self, user):
        if self.num_of_tacos > 0:
            self.num_of_tacos -= 1
            user.give_a_taco += 1
        else:
            print("No more taco to be given away")

    def __str__(self):
        return "{}, {} points, {} tacos left".format(self.name, self.score, self.num_of_tacos)
    
    
        