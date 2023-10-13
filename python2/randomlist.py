#!/bin/python3
# Req: generate a random list of size next
# n is from STDIN
# the list start and finish values are from STDIN
# Calculate and show the min, max, sum 

import random as ran 

start = int(input('Start: '))
finish = int(input('Finish: '))
n = int(input('Size: '))
try:
    numbers = ran.sample(range(start,finish),n)
    print(numbers)
except ValueError:
    print('Please do the right thing')
    start = int(input('Start: '))
    finish = int(input('Finish: '))
    n = int(input('Size: '))
    numbers = ran.sample(range(start,finish),n)
    print(numbers)

print(f'SUM = {sum(numbers)}')
print(f'MIN = {min(numbers)}')
print(f'MAX = {max(numbers)}')

