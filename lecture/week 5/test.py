names = ["Tony", "Saran", "Jennifer"]
ages = [40, 30, 25]

name_to_ages = {"Tony" : 40, "Saran" : 30, "Jennifer" : 25}
my_dict = name_to_ages
my_dict2 = name_to_ages.copy()

print(name_to_ages)
print(name_to_ages.keys())
print(name_to_ages["Tony"])
name_to_ages["Tony"] = 50
print(name_to_ages["Tony"])

print(my_dict["Tony"])
print(my_dict2["Tony"])


for key in my_dict2:
    print(key)

for key, value in my_dict2.item():
    print("{:4d} - {}".format(key, value))

