import sys
from random import randint

def main():
    output_file = open('unsorted.txt', 'w')
    number_of_numbers = (2000000*10)

    for x in xrange(0, number_of_numbers):
        output_file.write(str(randint(1000000000, 9999999999)) + '\n')

    output_file.close()

main()
