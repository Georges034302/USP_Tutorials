#!/bin/env python3

# Read integers from STDIN until -1
# Determine the min and max values
import sys 

n = int(input('n = '))

current_min = sys.maxsize
current_max = -sys.maxsize

while n != -1:
    if n > current_max:
        current_max = n 
    if n < current_min:
        current_min = n
    n = int(input('n = '))
print(f'Min = {current_min}')
print(f'Max = {current_max}')
