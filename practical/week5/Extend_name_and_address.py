print("Extend your name & address program with file loading and saving")
print("Saving : S")
print("Loading : L")
print("Exit : E")

a = False

while True:
    answer = input("What do you want to do? ")

    if answer == "S":
        information_file = open("information.txt", "w")
        name = input("What is your name and address? (Name/address) ")
        name = name.split("/")
        information_file.write(" ".join(name))
        information_file.write("\n")
        information_file.close()

    elif answer == "L":
        information_file = open("information.txt", "r")
        while True:
            line = information_file.readline()
            if not line:
                break
            print(line, end="")

    elif answer == "E":
        print("Finish program.")
        break
