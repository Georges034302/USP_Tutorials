#!/bin/env python3
# Dictionary is a data collection represented as key-value
# Dictionary is unordered
# Dictionary is indexed
# Dictionary is changeable
# Dictionary does not allow duplicates 

# create a dictionary of n - students with key-value representation
# key is a random 6-digits
# value is a name from STDIN

import random as r

students = {}                               #creating empty dictionary
n = int(input("N = "))

IDs = r.sample(range(100000,999999),n)     #generate a range and randomize n selection
print(f'IDs = {IDs}')

for key in IDs:
    students[key] = input("Name = ")

print(students)                             #print a dictionary

for key in sorted(students.keys()):
    print(f'{key} ---> {students[key]}')

key = int(input("Delete by key: "))
if key in IDs:
    del students[key]
else:
    print("Student does not exist in the list")
print(students)



