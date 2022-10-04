#!/bin/env python
#Generate a random list from first to last of size n
#first, last and n are from STDIN
#Determine and show the min and max

import random as ran
import sys

n= int(input("Size: "))
first = int(input("First: "))
last = int(input("Last: "))

numbers = ran.sample(range(first,last),n)
print(numbers)

smallest = sys.maxsize
biggest = 0

for e in numbers:
    if smallest > e:
        smallest = e
    if biggest < e:
        biggest = e

print(f'Min = {smallest}')
print(f'Max = {biggest}')
