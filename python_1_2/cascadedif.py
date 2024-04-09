#!/bin/env python3
import sys

# Enter a name from STDIN
# Get a mark from argument
# Determine and show the student grade

name = input('Name: ')
mark = int(sys.argv[1]) # argv values are all strings

if mark >= 85:
    grade = 'HD'
elif mark >= 75:
    grade = 'D'
elif mark >= 65:
    grade = 'C'
elif mark >= 50:
    grade = 'P'
else:
    grade = 'Z'

print(f'{name} mark is {mark} and grade is {grade}')