names = ["Jack", "Jill", "Harry"]
dates_of_birth = [(12, 4, 1999), (1, 1, 2000), (27, 3, 1982)]

name_to_DOB = {}

for i in range(3):
    name_to_DOB[names[i]] = dates_of_birth[i]

print(name_to_DOB.items())