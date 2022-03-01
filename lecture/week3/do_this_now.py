valid_input = False

while not valid_input:
    try:
        age = int(input("Age : "))
        if age > 0:
          valid_input = True
        else:
            print("age can not be negative.")
    except ValueError:
        print("Invalid (not an integer).")

if age % 2:
    print("{} is odd.".format(age))
else:
    print("{} is even.".format(age))

