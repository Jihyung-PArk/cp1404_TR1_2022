'''
1. Write code that asks the user for their name,
   then opens a file called "name.txt" and writes that
   name to it.
'''
name_file = "name.txt"
name_out_file = open(name_file, 'w')

name = input("What is your name? ")
name_out_file.write(name)
name_out_file.close()

'''
2. Write code that opens "name.txt" and reads the name
   (as above) then prints,
   "your name is Bob" (or whatever the name is in the file).
'''

name_out_file = open(name_file, 'r')
print("Your name is {}".format(name_out_file.read()))
name_out_file.close()

'''
3. Create a text file called numbers.txt and save it in your prac_02 directory. 
Put the following three numbers on separate lines in the file and save it:
17
42
400
Write code that opens "numbers.txt", reads only the first two numbers 
and adds them together then prints the result, which should be... 59.
'''

num_file = "numbers.txt"
num_output_file = open(num_file, 'r')
num1 = int(num_output_file.readline())
num2 = int(num_output_file.readline())
print(num1 + num2)
num_output_file.close()

'''
4. Now write a fourth block of code that prints the total for all lines in numbers.
   txt or a file with any number of numbers.
'''
sum = 0
num_output_file = open(num_file, 'r')
for line in num_output_file:
    num = int(line)
    sum += num
print(sum)