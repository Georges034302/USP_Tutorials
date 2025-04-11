#!/bin/env python3
# Read integers from STDIN until -1
# Caculcate and show the following:
# 1. Sum of the integers
# 2. Average of the integers
# 3. Maximum of the integers
# 4. Minimum of the integers
import sys

total = 0
count = 0
maximum = -sys.maxsize
minimum = sys.maxsize

n = int(input('n = '))

while n != -1:
    total += n
    count += 1
    if n > maximum:
        maximum = n
    if n < minimum:
        minimum = n
    n = int(input('n = '))

print(f'Total = {total}')
print(f'Average = {total/count:.3f}')
print(f'Maximum = {maximum}')
print(f'Minimum = {minimum}')