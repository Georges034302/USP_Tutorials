#!/bin/env python
#read an integer from STDIN until -1
#calculate and show the average values

n = int(input("N = "))
total = 0
count = 0
while n != -1:
    total += n 
    count += 1
    n = int(input("N = "))

print(f'Average = {total/count:.3f}')
