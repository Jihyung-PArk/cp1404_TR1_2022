"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

from random import*

def main():

    # score = float(input("Enter score: "))
    score_result(score)


def score_result(score):
    if score < 0:
        print("Invalid score")
    else:
        if score > 100:
            print("Invalid score")
        elif 100 >= score > 90:
            print("Excellent")
        elif 90 >= score > 50:
            print("Passable")
        else:
            print("Bad")

score = randint(-10,100)
print(score)

main()

