character = input("Enter a character: ")
print("The ASCII code for {} is {}".format(character, ord(character)))
character_given = False
while not character_given:
    try:
        given_character = int(input("Enter a number between 33 and 127: "))
        if 33<= given_character <=127:
            character_given = True
    except given_character < 33 or given_character >127:
        print("Enter a number between 33 and 127: ")
        character_given = False

print("The character for {} is {}".format(given_character, chr(given_character)))




for number in range(33,128):
    print("{:>3}  {}".format(number,chr(number)))