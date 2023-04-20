#!/bin/env python
#Generate a range of integers between start,finish, and step
#start, step and finish are from STDIN
#Calculate the sum and average
#Display the sum and average

start = int(input("Start: "))
finish = int(input("Finish: "))
step = int(input("Step: "))

numbers = list(range(start,finish,step))
print(numbers)

total = 0
for e in numbers:
    total += e

print(f'Sum = {total}')
print(f'Average = {total/len(numbers):.3f}')
