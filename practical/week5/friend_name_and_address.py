
def main ():

    name_to_address = {}

    print("Enter a new name & address : enter")
    print("Change an address for an existing entry : change")
    print("Print the address for a name you choose : print")
    print("If you want to finish entry : quit")
    choice =input("What is your coice? : ")

    while choice != "quit":

        if choice == "enter":
            name = input("What is friend's name? : ")
            while name == "no more":
                address = input("What is your address? : ")
                name_to_address[name] = address
                print("If no more friends, enter \"no more\".")
                name = input("What is friend's name? : ")




        elif choice == "change":
            choice_name = input("whose address are you going to change? : ")
            choice_address = input("What is new address? : ")
            name_to_address[choice_name] = choice_address


        elif choice == "print":
            name_print = input("Whose address are you going to print? : ")
            print(name_to_address[name_print])




main()