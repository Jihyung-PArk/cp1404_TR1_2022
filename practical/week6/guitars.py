from guitar import Guitar

def main():
    guitar_list = []

    print("My guitar!")

    name = input("name : ")
    while name != "":
        year = int(input("year : "))
        cost = float(input("cost : "))
        print("{} ({}) : ${} added.".format(name, year, cost))
        add = Guitar(name, year, cost)
        guitar_list.append(add)
        # check point
        print(guitar_list[0])
        name = input("name : ")

    print("There are my guitars:")
    for i in range(0, len(guitar_list)):
        print("Guitar {} : {}".format(i+1, guitar_list))


main()