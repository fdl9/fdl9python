"""
TODO: edit this code so that:
    1) to_read.txt is now called read_write.txt and can be used for both reading and writing
        -see how to open a file for read and write
        -see documentation around the seek() method

    2) read_write.txt is removed at the end of our run
    3) write to output.txt instead of writing to stdout (i.e. printing to the terminal)
"""

# Operating system access (allows for path finding, calling command line, ...)
import os


# open file to write
to_read_write_file_pointer = open("read_write.txt", 'w+')
to_write_file_pointer = open("output.txt", 'w')

# FOR: number in range from 1 to 10, write the number and a new line to our file
for number in range(1, 10):
    # write number to file (with a new line)
    to_read_write_file_pointer.write("{0}\n".format(number))

# create a list of letters to output to our file
letters = ['a', 'b', 'c', 'd', 'e']

# FOR: letter in letters from a to e, write letter and a new line to our file
for letter in letters:
    # write letter to file (with a new line)
    to_read_write_file_pointer.write("{0}\n".format(letter))

# go back to beginning of file
to_read_write_file_pointer.seek(0)

# FOR: line in to_read_file_pointer, read and print each line
for line in to_read_write_file_pointer:
    # print line
    # print("Line: {0}".format(line))
    # write to file
    to_write_file_pointer.write("{0}".format(line))

# close files
to_read_write_file_pointer.close()
to_write_file_pointer.close()

# Uncomment the line below to remove temp file after reading is done
os.remove("read_write.txt")

