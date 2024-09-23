#!/bin/env python3

# Read integer n until -1
# Add and show the total even value 

n = int(input('n = '))
total = 0

while n != -1:
    if n%2 == 0:
        total += n
    n = int(input('n = '))
print(f'Even sum = {total}')
