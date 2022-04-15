from sliver_service_taxi import SliverServiceTaxi
from taxi import Taxi
from car import Car


def main():

    MENU = "q)uit, c)hoose, d)rive"
    taxis = [Taxi("Prius", 100), SliverServiceTaxi("Limo", 100, 2), SliverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill = 0

    print("Let's drive!")
    print(MENU)
    menu_choose = input(">>> ").lower()

    while menu_choose != "q":
        if menu_choose == "c":
            print("Taxi available : ")
            choose(taxis)
            choose_taxi = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[choose_taxi]
            except IndexError:
                print("invalid taxi choice")

        elif menu_choose == "d":
            if current_taxi:
                current_taxi.start_fare()
                distance = float(input("Drive how far? "))
                current_taxi.drive(distance)
                cost = current_taxi.get_fare()
                print("Your {} trip cost you ${:.2f}".format(current_taxi.name, cost))
                bill += cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print("Bill to date : ${:.2f}".format(bill))
        print(MENU)
        menu_choose = input(">>> ").lower()

    print("Total trip cost: ${:.2f}".format(bill))
    print("Taxis are now: ")
    choose(taxis)

def choose(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))



main()
