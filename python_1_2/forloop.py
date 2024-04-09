#!/bin/env python3

# Read integer n from STDIN
# Display all values and their square from 0 to n 
# ensure that each value is allocated 4 spaces

n = int(input('n = '))

for e in range(0,n+1):
    print(f'{e:<4} --> {pow(e,2):<4}')