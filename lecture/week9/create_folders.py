import os
import csv

file = "cp1111.csv"
path = "."  # . means current directory

def get_usernames(csv_file):
    username_list = []
    try:
        infile = open(csv_file, 'r')
        reader = csv.reader(infile)
        for row in reader:
            # row is a list of strings, username is the 3rd column
            if len(row) != 0:
                username_list.append(row[2])
        infile.close()

        if len(username_list) == 0:
            print("Empty")
        else:
            print("{} usernames loaded".format(len(username_list)))

    except IOError as error:
            print("I/O error : {}".format(error))

    return username_list

user_list = get_usernames(file)
for username in user_list:
    user_path = path + '//' + username
    if not os.path.exists(user_path):
        os.makedirs(user_path)
    else:
        print(username, 'is already created.')