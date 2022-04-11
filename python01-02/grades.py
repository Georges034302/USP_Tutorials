#!/bin/env python3
#Read Student name from STDIN
#Capture the mark from argument 
#Display the grade for the student 
import sys

name = input("Student name: ")
mark = int(sys.argv[1])

if mark >= 85:
    grade = "HD"
elif mark >= 75:
    grade = "D"
elif mark >= 65:
    grade = "C"
elif mark >= 50:
    grade = "P"
else:
    grade = "Z"

print(f'Student {name} has mark {mark} and grade {grade}')
