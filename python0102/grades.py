#!/bin/env python3

import sys

name = input("Student: ")

mark = int(sys.argv[1])

if(mark >= 85):
    grade = "HD"
elif (mark >= 75):
    grade = "D"
elif(mark >= 65):
    grade = "C"
elif(mark >= 50):
    grade = "P"
else:
    grade = "Z"

result = "Welcome {} Your mark is {:_^4} and your grade is {:-^4}"
print(result.format(name,mark,grade))
