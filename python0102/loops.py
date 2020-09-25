#!/bin/env python3

s = input("String: ")

for e in s:
    print(e, end=" ")
print()

i = 0
while i < len(s):
    print(s[i], end=",")
    i+=1
print()

num = int(input("Value: "))

i = 0
nsum = 0
while i <= num:
    nsum += num
    i +=1
print ("Sum = "+str(nsum))
