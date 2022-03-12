numbers = []

num_print = 0
num_count = 0
num = int(input("number : "))


while True:
    if num >=1:
        num_count += 1
        numbers.append(num)
        num = int(input("number : "))

        continue

    else:
        break


# print(num_count)
# print(numbers)
while True:
    if num_print != num_count:
        print("Number {} : {}".format(num_print+1, numbers[num_print]))
        num_print += 1
        continue
    else:
        break



print("The first number is {}".format(numbers[0]))
print("THe last number is {}".format(numbers[-1]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))
print("The average of the number is {}".format(sum(numbers)/len(numbers)))



usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
name = input("Username : ")
check_name = name in usernames


if check_name == True:
    print("Access granted")
elif check_name == False:
    print("Access denied")

# 3. check Duplicate in list
check_duplicate = []
duplicate = []
while True:
    ent_input = input("Enter string : ")

    if not ent_input:
        break

    check_duplicate.append(ent_input)

check = sorted(check_duplicate)

for i in check:
     if check.count(i)>1:
         if i not in duplicate:
             duplicate.append(i)
# print(check_duplicate)
# print(duplicate)

if len(duplicate) > 0:
    duplicate_exit = (','.join(duplicate))

    print("String reqeated : {}".format(duplicate_exit))
else:
    print("No repeated strings entered.")

#4. Memberwise Addition

list1 = [1, 2, 3, 4]
list2 = [1, 2, 3]
result = []


def memberwise():
    if len(list1) >= len(list2):
        len1 = len(list1) - len(list2)
        for i in range(0, len1):
            list2.append(0)
        for i in range(0, len(list1)):
            result.append(list1[i] + list2[i])

    elif len(list1) < len(list2):
        len2 = len(list2) - len(list1)
        for i in range(0, len2):
            list1.append(0)
        for i in range(0, len(list2)):
            result.append(list1[i] + list2[i])


memberwise()


print(" Resultant list : " + str(result))