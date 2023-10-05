#!/bin/python3
# Req: Read values from STDIN until -1
# Add all the even values
# Show the maximum value
# Show the average value 
import sys

value = int(input('Value = '))
total = 0
maximum = -sys.maxsize
count = 0

while value != -1:
    if value %2 == 0:
        total += value

    if value >= maximum:
        maximum = value

    count +=1
    value = int(input('Value = '))

print(f'Total = {total}')
print(f'Max = {maximum}')
print(f'Average = {total/count:.2f}')


