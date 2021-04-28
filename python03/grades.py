#!/bin/env python3
#define a script that reads student name from stdin
#and reads the mark from argument
#then determine the grades

import sys 

name = input("Student: ")
mark = int(sys.argv[1])

if(mark >= 85):
    grade = "HD"
elif(mark >= 75):
    grade = "D"
elif(mark >= 65):
    grade = "C"
elif(mark >= 50):
    grade = "P"
else:
    grade="Z"

result = "Welcome {} your mark is {:^8} and your grade is {}"
print(result.format(name,mark,grade))
