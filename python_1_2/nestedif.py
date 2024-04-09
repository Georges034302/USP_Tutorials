#!/bin/env python3

# Enter a value from STDIN
# Check if the value is even, odd, or negative

n = int(input('N = ')) # input always gives back a string

if n > 0:
    if n%2 == 0:
        print(f'{n} is even')
    else:
        print(f'{n} is odd')
else:
    print(f'{n} is negative')