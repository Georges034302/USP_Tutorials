#!/bin/env python3

# Read n integer from STDIN
# Determine the factorial of n

n = int(input('n = '))

f = 1

for e in range(2,n+1):
    f *= e

print(f'factorial({n}) = {f}') 
