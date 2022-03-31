"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    # add new car name limo and fuel 100
    limo = Car("limo", 100)

    # check new car condition
    # print("About new car >>> name : {}, fuel : {}

    # add fuel 20
    limo.add_fuel(20)

    # check add_fuel
    # print("check current fuel >>> name : {}, fuel : {}".format(limo.name, limo.fuel))

    print("Amount of fuel >>> name : {}, fuel : {}.".format(limo.name, limo.fuel))

    # move 115km
    limo.drive(115)

    # check odometer
    print("odometer >>> name : {}, odometer : {}".format(limo.name, limo.odometer))

    # check __str__
    print(limo)

main()