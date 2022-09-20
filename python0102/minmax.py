#!/bin/env python

#Read integers until -1
#Determine and show the min and the max of the entered values

n = int(input("N = "))

minimum = 0;
maximum = 0;

while n != -1:
    if(minimum > n):
        minimum = n
    if(maximum < n):
        maximum = n 

    n = int(input("N = "))

print(f'Min = {minimum}')
print(f'Max = {maximum}')
