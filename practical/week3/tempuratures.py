"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""



def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = fah_temp(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            # TODO: Write this section to convert F to C and display the result
            # Hint: celsius = 5 / 9 * (fahrenheit - 32)
            # Remove the "pass" statement when you are done. It's a placeholder.
            fahrenheit = float(input("Fahrenheit: "))
            celsius = cel_temp(fahrenheit)
            print("Result: {:.2f}C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def cel_temp(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def fah_temp( celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit



main()
