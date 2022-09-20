#!/bin/env python

s = input("String: ")

for e in s:
    print(e,end=", ")
print()

i = 0
while i < len(s):
    print(s[i])
    i+=1
