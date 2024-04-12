#!/bin/env python3

# Read integers from STDIN until -1
# Caculate and show the even-sum, max, min
import sys 

n = int(input('n = '))
total = 0
maximum = -sys.maxsize
minimum = sys.maxsize

while n != -1:
    if n%2 == 0:
        total += n 
    if maximum < n:
        maximum = n 
    if minimum > n:
        minimum = n   
    n = int(input('n = '))

print(f'Even-Sum = {total}')
print(f'Min = {minimum}')
print(f'Max = {maximum}')
