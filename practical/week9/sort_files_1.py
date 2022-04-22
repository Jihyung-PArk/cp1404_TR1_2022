import os

def main():
    os.chdir("FilesToSort")
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        filename_extension = filename.split(".")[1]
        try:
            os.mkdir(filename_extension)
        except FileExistsError:
            pass

        os.rename(filename, "{}/{}".format(filename_extension, filename))


main()

