import csv

def test_file(infile):

    try:
        infile = open(infile, 'r')
        file_reader = csv.reader(infile)
        outfile = open('outputfile.txt', 'w')
        file_writer = csv.writer(outfile)
        for row in file_reader:
            file_writer.writerow(row)
        infile.close()
        outfile.close()
    except IOError as error:
        print("I/O error: {}".format(error))


test_file('inputfile.txt')


    