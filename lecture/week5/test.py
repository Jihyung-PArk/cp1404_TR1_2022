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

for key, value in my_dict2.items():
    print("{:10s} - {:10d}".format(key, value))

name_to_age = {"Bill" : 17, "Jane" : 34, "Jack" : 56, "Sven" : 13}
    # result = {name: age for name, age in name_to_age.items() if age < 18}
# print(result)

result = { }
for name, age in name_to_age.items():
    if age < 18:
        result[name] = age

print(result)