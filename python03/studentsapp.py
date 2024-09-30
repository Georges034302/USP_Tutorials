#!/bin/env python3

# Develop a student application as follows:
# - Register 3 students with random ID of 3-digits size
# - Each student name is read from STDIN
# - show the student data structure
import pprint as pp 
import random as ran 

ids = ran.sample(range(100,1000),3) # list of 3 random IDs 
students = []

for key in ids:
    student = {}
    student['ID'] = key 
    student['name'] = input('Name: ')
    students.append(student)
pp.pprint(students,indent=2, width=20)

