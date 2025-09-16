#!/bin/env python3
import math as m 


# Read n integer from STDIN until -1
# Calculcate and show the factorial of n
n = int(input('n = '))

# Method 1
# while n != -1:
#     f = 1
#     for e in range(2,n+1):
#         f *= e 
#     print(f'Factorial({n}) = {f}')
#     n = int(input('n = '))

# Method 2
while n != -1:
    print(f'Factorial({n}) = {m.factorial(n)}')
    n = int(input('n = '))




