#!/bin/env python3
#Read a string from STDIN and print the characters seperated by a space 
#Read a number from argument and print a sequence of numbers from zero to that number

import sys 

s = input("String: ")
s1 = s.upper()
for c in s1:
    print(c, end=" ")
print()

n = int(sys.argv[1])
i = 0
nsum =0
while i <= n:
    p = pow(i,2)
    nsum += i
    print("i = {} and power = {} ".format(i,p))
    i+=1
print("sum = "+str(nsum))

