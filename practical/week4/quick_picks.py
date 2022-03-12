import random


line_consist = 6
minimum = 1
maximum = 45


def main():
    picks = int(input("How many quick picks? "))

    for num in range(picks):
        quick_pick = []
        for list_num in range(line_consist):
            number = random.randint(minimum, maximum)
            while number in quick_pick:
                number = random.randint(minimum, maximum)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()