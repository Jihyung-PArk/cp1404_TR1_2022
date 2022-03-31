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
        # print(guitar_list[0])
        name = input("name : ")

    guitar_list.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitar_list.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if len(guitar_list) != 0:
        print("There are my guitars:")

        for i, guiter in enumerate(guitar_list):
            vintage = ""
            if guiter.is_vintage():
                vintage = "    (vintage)"
            print("Guitar {0} : {1.name}({1.year}), worth ${1.cost:10,.2f}{2}".format(i + 1, guiter, vintage))


main()
