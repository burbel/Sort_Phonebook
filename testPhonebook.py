import sys

def main():
    test_file = open('phonebook.txt')

    current_number = 0
    current_line = ' '

    while (current_line):
        current_line = test_file.readline()
        if (current_line):
            new_number = int(current_line)
            assert (new_number >= current_number)
            current_number = new_number

    test_file.close()

main()
