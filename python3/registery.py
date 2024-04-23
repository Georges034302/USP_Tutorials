#!/bin/env python3

# Register 3 students as follows
# Student ID is random of size 3 digits
# Student Name from STDIN

import random as ran
import pprint as pp

ids = ran.sample(range(100,1000),3)

students = {}

for id in ids:
    students[id] = input('Name: ')

pp.pprint(students,width=30)
