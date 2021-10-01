#!/bin/env python3
#read student name and marks from STDIN and print the grade

name = input("Name: ")
mark = int(input("Mark: "))

if(mark >= 85):
    grade = "HD"
elif(mark >= 75):
    grade = "D"
elif(mark >= 65):
    grade = "C"
elif(mark >= 50):
    grade = "P"
else:
    grade = "Z"

print("{} grade is: {}".format(name,grade))
