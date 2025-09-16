#!/bin/env python3

# Read integer values from STDIN until -1
# Calculate and show the total and average


n = int(input('n = '))

total = 0
count = 0

while n != -1:
    total += n 
    count += 1
    n = int(input('n = '))
print(f'Total = {total}')
print(f'Average = {total/count}')
