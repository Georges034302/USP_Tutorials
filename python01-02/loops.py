#!/bin/env python3

#Read a string from STDIN
#Print each character on a new line
s = input("String: ")

txt =""
for e in s:
    #print(e)
    txt += e+","
    #print(e, end=", ")
print(txt.strip(","))

num = int(input("Number: "))
i = 0
total = 0

while i <= num:
    total += i
    i+=1
print("Total = ",total)
