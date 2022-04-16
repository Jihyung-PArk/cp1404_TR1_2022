from taxi import Taxi

class EcoTaxi(Taxi):

    def __init__(self, name, fuel):
        super().__init__(name, fuel)

    def __str__(self):
        return "{}".format(super().__str__())

    def discount_price(self):
        price_per_km = super().price_per_km
        return price_per_km / 0.8

    def half_fuel(self):
        fuel = super().fuel
        return fuel / 2


