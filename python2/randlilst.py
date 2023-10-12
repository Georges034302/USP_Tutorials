#!/bin/python3
#Req: create a random list from start to finish
# from STDIN
# Read the size of the list from STDIN
import random as ran 

start = int(input('start = '))
finish = int(input('finish = '))
n = int(input('size = '))

numbers = ran.sample(range(start,finish+1),n)
print(numbers)
numbers.reverse()
print(numbers)

print(f'SUM = {sum(numbers)}')
print(f'MIN = {min(numbers)}')
print(f'MAX = {max(numbers)}')

