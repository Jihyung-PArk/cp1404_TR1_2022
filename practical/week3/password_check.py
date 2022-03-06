min_length = 10


def main():

    password = get_password()
    password_length = False


    while not password_length:

        if len(password) >= 10:
            print_password = "*" * len(password)
            the_password(print_password)
            password_length = True


        elif len(password) < 10:
            password = get_password()
            password_length = False


def get_password():
    password = input("password : ")
    return password

def the_password(print_password):
    print(print_password)


main()





