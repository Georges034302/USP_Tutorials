#!/bin/env python3

s = input("String: ")

for e in s:
    print(e)

i = 0
while i < len(s):
    print(s[i], end=" ")
    i+=1
print()
