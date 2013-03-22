import sys

def chunkUnsorted(phonebook_size, number_of_chunks):
# Break the single unsorted.txt phonebook into number_of_chunk sorted files within temp/
# Takes roughly 20% of the processing time of this program

    unsorted_file = open('unsorted.txt', 'r')

    chunk_size = phonebook_size/number_of_chunks

    current_line = ' '
    current_temp_file = 0

    while (current_line):
        list = []
        x = 0
        while (current_line and (x < chunk_size)):
            current_line = unsorted_file.readline()
            if (current_line):
                list.append(int(current_line))
                x += 1
        list.sort()
        if list:
            filename = "temp/chunk%d.txt" % current_temp_file
            current_temp_file += 1
            output_file = open(filename, 'w')
            for x in list:
                output_file.write(str(x) + '\n')
            output_file.close()

    unsorted_file.close()

def sortPhonebook(phonebook_size, number_of_chunks):
# Create a list of number_of_chunk file pointers and a corresponding list of the first values in each file
# Iterate over phonebook_size adding the min value to the output and swapping the appropriate entry in lowestValues
# Takes roughly 80% of the processing time of this program

    fid = [open('temp/chunk%d.txt' % count, 'r') for count in range(0, number_of_chunks)]
    lowestValues = [int(fid[count].readline()) for count in range(0, number_of_chunks)]

    output_file = open('phonebook.txt', 'w')

    for x in xrange(0, phonebook_size):
        lowest_location = lowestValues.index(min(lowestValues))
        output_file.write(str(lowestValues[lowest_location]) + '\n')
        temp = fid[lowest_location].readline()
        if (temp):
            lowestValues[lowest_location] = int(temp)
        else:
            lowestValues[lowest_location] = 12345678987
            fid[lowest_location].close()

    output_file.close()

chunkUnsorted((2000000*10), 200)
sortPhonebook((2000000*10), 200)

