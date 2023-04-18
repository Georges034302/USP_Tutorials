#!/bin/python3
# Read values from STDIN until -1
# Determine and show the min and max
# Determine the total value

import sys
maximum = -sys.maxsize
minimum = sys.maxsize

value = int(input("Value = "))
total = 0

while value != -1:
    if value > maximum:
        maximum = value 
    if value < minimum:
        minimum = value 
    total += value
    value = int(input("Value = "))

if total > 0:
    print(f'Max = {maximum}')
    print(f'Min = {minimum}')
    print(f'Total = {total}')
else:
    print("Values not entered")