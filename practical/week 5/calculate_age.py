'''
names = ["Jack", "Jill", "Harry"]
dates_of_birth = [(12, 4, 1999), (1, 1, 2000), (27, 3, 1982)]
'''
def main():

    name_to_birth = {}
    print("the user to enter the date-of-birth details for 5 people.")

    for i in range(5):
        name = input("name : ")
        date_of_birth = input("date of birth (D/M/Y) : ")
        date_of_birth = date_of_birth.split("/")
        date_of_birth = (int(date_of_birth[0]), int(date_of_birth[1]), int(date_of_birth[2]))
        current_age = calculate_age(date_of_birth)
        name_to_birth[name] = current_age
    for key in name_to_birth.items():
        print(key)


def calculate_age (date_of_birth):
    today = [18, 3, 2022]
    if today[1] > date_of_birth[1]:
        age = today[2] - date_of_birth[2]
        return age
    elif today[1] == date_of_birth[1] and today[0] > date_of_birth[0]:
        age = today[2] - date_of_birth[2]
        return age
    elif today[1] < date_of_birth[1]:
        age = today[2] - date_of_birth[2] - 1
        return age
    elif today[1] == date_of_birth[1] and today[0] < date_of_birth[0]:
        age = today[2] - date_of_birth[2] - 1
        return age
    elif today[1] == date_of_birth[1] and today[0] == date_of_birth[0]:
        age = today[2] - date_of_birth[2]
        return age

main()

