import csv

def longest_line(infile):
    longest_line_num = 0
    longest_str = ""
    line_number = 0

    try:
        infile = open(infile, 'r')
        for line in infile:
            line_number += 1
            if len(longest_str) < len(line.strip()):
                longest_str = line
                longest_line_num = line_number
        infile.close()
        print("Line {} is the longest line with {} chracters"
              .format(longest_line_num, len(longest_str)))
    except IOError as error:
        print("I/O error: {}".format(error))

    return longest_line_num, len(longest_str)

print(longest_line('inputfile.txt'))

open('inputfile.txt', 'r') as in_file:

    