from car import Car

menu = "menu: \ d) drive \ r) refuel \ q) quit"

def main():

    print("Let's drive!")

    car_name = input("Enter your car name : ")

    car = Car(car_name, 100)
    print(car)
    print(menu)
    choice = input("Enter your choice : ").lower()

    while choice != "q":
        if choice == "d":
            drive_km = int(input("How many km do you wish to drive?"))
            while drive_km < 0:
                print("Distance must be >= 0")
                drive_km = int(input("How many km do you wish to drive?"))
            distance = car.drive(drive_km)

            if car.fuel == 0:
                print("The car drove {}km and ran out of fuel.".format(distance))
            else:
                print("The car drove {}km".format(distance))

        elif choice == "r":
            add = int(input("How many units of fuel do you want to add to the car?"))
            while add < 0:
                print("Fuel amount must be >= 0")
                add = int(input("How many units of fuel do you want to add to the car?"))
            car.add_fuel(add)
            print("Added {} units of fuel.".format(add))


        else:
            print("Invalid choice")

        print(car)
        print(menu)
        choice = input("Enter your choice : ").lower()

    print("\nGood bye {}'s driver.".format(car.name))

main()

