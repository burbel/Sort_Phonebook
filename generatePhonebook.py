import sys
import random

output_file = open('book.txt', 'w')

for x in xrange(0, (2000000*1)):
    line = str(random.randint(1000000000, 9999999999)) + '\n'
    output_file.write(line)

output_file.close()

