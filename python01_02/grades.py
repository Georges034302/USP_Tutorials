#!/bin/python3
import sys 

# Enter student name from STDIN
# Get the mark from argument
# Determine and show grade based on the mark

name = input('Name: ')
mark = int(sys.argv[1])

if mark >= 85:
    grade = 'HD'
elif mark >= 75:
    grade = 'D'
elif mark >= 65:
    grade = 'P'
elif mark >= 50:
    grade = 'C'
else:
    grade = 'Z'
print(f'{name} mark is {mark} and grade is {grade}')

