import shutil
import os


def main():
    print("Starting directory is: {}".format(os.getcwd()))
    os.chdir('Lyrics/Christmas')
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    for directory_name, subdirectories, filenames in os.walk('.'):

        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))
            new_name_two = get_fixed_filename_two(filename)
            print("Renaming {} to {}".format(filename, new_name_two))
            # current_name = os.path.join(directory_name, filename)
            # new_name = os.path.join(directory_name, new_name)
            # os.rename(current_name, new_name)


def get_fixed_filename_two(filename):
    character_num = 1
    character = []
    for characters in enumerate(filename):
        character.append(characters)

    while character_num == len(character):
        for i in range(len(character) - 1):

            if character[i][1].islower() and character[i + 1][1].isupper():
                new_name = filename.replace(character[i + 1][1], "_" + character[i + 1][1])

            elif character[i][1].isupper() and character[i + 1][1].isupper():
                new_name = filename.replace(character[i + 1][1], "_" + character[i + 1][1])

            character_num += 1




def get_fixed_filename(filename):
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name

    return new_name


main()
