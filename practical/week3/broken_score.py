"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))
if score < 0:
    print("Invalid score")
else:
    if score > 100:
        print("Invalid score")
    elif 100 >= score > 90:
        print("Excellent")
    elif 90>= score > 50:
        print("Passable")
    else:
        print("Bad")