from car import Car
from random import *

class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_range = randrange(1, 101)
        if random_range >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven

