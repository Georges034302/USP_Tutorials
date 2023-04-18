#!/bin/python3

# Read the name from STDIN
# Get the mark from args

import sys

name = input("Name: ")
mark = int(sys.argv[1])

if mark >= 85:
    grade = "HD"
elif mark >= 75:
    grade = "D"
elif mark >= 65:
    grade = "C"
elif mark >= 50:
    grade = "C"
else:
    grade = "Z"

print(f'{name} mark is {mark} and grade is {grade}')