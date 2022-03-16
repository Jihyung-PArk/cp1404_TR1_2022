
colour = {"Absolute Zero" : "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "#f0f8ff",
            "Alizarin crimson": "#e32636", "Amaranth": "#e52b50", "Amber": "#ffbf00",
            "Amethyst": "#9966cc", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb",
            "AntiqueWhite2": "#eedfcc", "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "##8b8378"}


name = input("Enter a colour name: ")


while name != " ":

    print("{0} is {1}".format(name, colour.get(name)))
    name = input("Enter a colour name: ")