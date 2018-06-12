import os
import sys

#open file to read
to_read_file_pointer = open("to read.txt", 'r')
a=0
for line in to_read_file_pointer:
    a = a + 1
    #print("Line:{0}".format(line))
    #print("index value is {1}, Line value is {0}".format(line,a))
    print("Line value is {0}, index value is {1}".format(line,a))
to_read_file_pointer.close()