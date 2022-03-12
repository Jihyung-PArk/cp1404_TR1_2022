numbers = [3, 1, 4, 1, 5, 9, 2]

'''
 numbers[0] = 3
 numbers[-1] = 2
 numbers[3] = 1
 numbers[:-1} = [3, 1, 4, 1, 5, 9]
 numbers[3:4] = 1
 5 in numbers = True
 7 in numbers = False
 "3" in numbers = False
 numbers + [6, 5, 3] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
  '''


# 1. change the first element of numbers to "ten"(the string, not the number 10)
numbers[0]= "ten"

# 2. change the last element of number to 1
numbers[-1] = 1

# 3. get all the elements from numbers except the first two (slice)
numbers[2:]

# 4. check if 9 is an element of numbers
9 in numbers
