import sys
import random

book_file = open('book.txt', 'r+')

number_of_chunks = 200 # I assume that number_of_chunks must evenly divide the total file
phonebook_size = (2000000*1)
chunk_size = phonebook_size/number_of_chunks
current_line = ' '
current_temp_file = 0

while (current_line):
    list = []
    x = 0
    while (current_line and (x < chunk_size)):
        current_line = book_file.readline()
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
    else:
        current_temp_file -= 1

book_file.close()

fid = [open('temp/chunk%d.txt' % count, 'r') for count in range(0, number_of_chunks)]
lowestValues = [int(fid[count].readline()) for count in range(0, number_of_chunks)]

# for each iteration I need to find the smallest remaining value in lowestValues that is valid (watch out for empty lists)
# Once I get the lowest, I write that to output_file
#  I also need to increment lowestValues[n] where n is the file that I found the lowestValue in

output_file = open('sorted.txt', 'w')

for x in xrange(0, phonebook_size):
    pass
    lowest_location = lowestValues.index(min(lowestValues))
    line = str(lowestValues[lowest_location]) + '\n'
    output_file.write(line)
    temp = fid[lowest_location].readline()
    if (temp):
        lowestValues[lowest_location] = int(temp)
    else:
        lowestValues[lowest_location] = 12345678987


output_file.close()



#for x in xrange(0, (2000000*1)):
#    line = str(random.randint(1000000000, 9999999999)) + '\n'
#    output_file.write(line)


