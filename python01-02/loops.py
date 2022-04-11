#!/bin/env python3

#Read a string from STDIN
#Print each character on a new line
s = input("String: ")

for e in s:
    #print(e)
    print(e, end=", ")
print()

num = int(input("Number: "))
i = 0
total = 0

while i <= num:
    total += i
    i+=1
print("Total = ",total)
