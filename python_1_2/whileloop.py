#!/bin/env python3

# Read integers from STDIN until -1
# Add all even values
# Show the total value

n = int(input('n = '))
total = 0

while n != -1:
    if n%2 == 0:
        total += n
    n = int(input('n = '))

print(f'Total = {total}')