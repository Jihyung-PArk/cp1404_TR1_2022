csv_file = "cp1111.csv"


def main():
    try:
        infile = open(csv_file, 'r')   # r = read, w = write, a = append
        num_user = 0
        for line in infile:
            num_user += 1
            temp_list = line.strip().split(',')
            print(temp_list[2])
        infile.close()
        print("{} items loaded from {}".format(num_user, csv_file))
    except IOError as err:
        print("I/O error: {0}".format(err))


# Start the program
main()
