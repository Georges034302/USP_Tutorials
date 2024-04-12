#!/bin/env python3

# Enter a value from STDIN
# check if the value is even, or negative

n = int(input('N = '))

if n >=0:
    if n%2 == 0:
        print(f'{n} is even')
    else:
        print(f'{n} is odd')
else:
    print(f'{n} is negative')
