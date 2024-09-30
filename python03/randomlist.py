#!/bin/env python3

# Generate a random list as follows:
# start from STDIN
# end from STDIN 
# size from STDIN 
# Determine the min, max, sum of values

import random as ran 

start = int(input('Start = '))
end = int(input('End = '))
n = int(input('Size = '))

numbers = ran.sample(range(start,end+1),n)
print(numbers)

print(f'Sum = {sum(numbers)}')
print(f'Min = {min(numbers)}')
print(f'Max = {max(numbers)}')
