import os

def main():

    os.chdir("FilesToSort")
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        filename_extension = filename.split(".")[1]
        extension = {}

        if filename_extension not in extension:
            input_directory = input("What category would you like to sort {} files into? ".format(filename_extension))
            extension[filename_extension] = input_directory

            try:
                os.mkdir(input_directory)
            except FileExistsError:
                pass

        os.rename(filename, "{}/{}".format(extension[filename_extension], filename))

main()