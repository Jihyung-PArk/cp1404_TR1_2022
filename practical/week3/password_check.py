min_length = 10
password = input("password : ")
password_length = False

while not password_length:

    if len(password) >= 10:
        length = len(password)
        print("*"*length)
        password_length = True

    elif len(password) < 10:
        password = input("password : ")
        password_length = False







