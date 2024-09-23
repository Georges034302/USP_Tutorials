#!/bin/env python3

# Read an integer n from STDIN
# Calculate and show the factorial n 

n = int(input('n = '))

f = 1

for e in range(2,n+1):
    f *= e

print(f'factorial({n}) = {f}')
