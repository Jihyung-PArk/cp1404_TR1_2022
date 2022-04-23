import os

def main():
    print("Starting directory is: {}".format(os.getcwd()))
    os.chdir('Lyrics/Christmas')
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    check_str = ".i"
    print("The file which missing copyright: ")
    for i in os.listdir('.'):
        with open(i, 'r') as file:
            read = file.read()
            if read.count(check_str):
                print("file name is {}\ndirectory of file is {}".format(i, os.getcwd()))



main()