#!/bin/python
import os

# Open a new file in write mode and append three lines
with open('new_file.txt', 'w') as file:
    file.write('This is line 1.\n')
    file.write('This is line 2.\n')
    file.write('This is line 3.\n')

# Open the file in read mode and print the first line to the screen
with open('new_file.txt', 'r') as file:
    print(file.readline())

# Delete the file
os.remove('new_file.txt')