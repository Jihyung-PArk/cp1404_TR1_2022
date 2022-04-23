import os


def main():
    print("Starting directory is: {}".format(os.getcwd()))
    menu = input("S = Size\nE = Extension\n>>>")
    if menu == "s":
        get_certain_size()
    elif menu == "e":
        get_certain_extension()


def get_certain_size():
    size_input = input("What size? : ")

    for i in os.listdir('.'):
        get_size = os.path.getsize(i)

        if int(get_size) >= int(size_input):
            print(i)


def get_certain_extension():
    extension_input = input("(add . infront of extension)\nWhat kind of extension do you want? : ")
    for i in os.listdir('.'):
        extension = os.path.splitext(i)[-1]

        if extension_input == extension:
            print(i)


main()
