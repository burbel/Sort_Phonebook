import sys

test_file = open('sorted.txt')

current_number = 0
current_line = ' '
while (current_line):
    current_line = test_file.readline()
    if (current_line):
        new_number = int(current_line)
        #assert (new_number >= current_number)
        if (new_number < current_number):
            print "New Number: %d, Current Number: %d" % (new_number, current_number)
        current_number = new_number

print "Test completed."

test_file.close()

