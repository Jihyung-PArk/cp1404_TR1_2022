"""
Testing for functions
"""
from math import *
import string


def main():
    print(sqrt(25))
    converted_degree = celsius_to_fahrenheit(100)
    print(converted_degree)
    print(count_letters("123abc"))


def celsius_to_fahrenheit(celsius):
    return celsius * 1.8 + 32.0

def count_letters(text):

    """Count the number of letters in text."""
    count = 0
    for character in text:
       if character.lower() in string.ascii_letters:
            count += 1
    return count


# start the program
main()
