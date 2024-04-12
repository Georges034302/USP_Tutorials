#!/bin/env python3

# Read positive integer n from STDIN
# Determine and show the formatted n values
# and the power n 

n = int(input('n = '))

for e in range(0,n+1):
    print(f'{e:<4} --> {pow(e,2):8}')
