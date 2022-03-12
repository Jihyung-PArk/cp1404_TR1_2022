numbers = []


numbers.append(int(input("input first number :")))
numbers.append(int(input("input first number :")))
numbers.append(int(input("input first number :")))
numbers.append(int(input("input first number :")))
numbers.append(int(input("input first number :")))

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