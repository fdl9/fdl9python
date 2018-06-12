import os
import sys

# print("hello world")

to_write_file_pointer= open('to read.txt','w')

for number in range (1,10):
    to_write_file_pointer.write("{}\n".format(number))

letters = ['a', 'b', 'c', 'd', 'e']

for i in letters:
    to_write_file_pointer.write("{}\n".format(i))

to_write_file_pointer.close()

