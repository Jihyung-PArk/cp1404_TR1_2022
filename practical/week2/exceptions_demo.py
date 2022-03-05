"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator(Natural Number): "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

'''
Questions
1. When will a ValueError occur?
  => When input non-numerical value
2. When will a ZeroDivisionError occur?
  => put the 0 on denominator
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
  => Yes, it is possible
'''