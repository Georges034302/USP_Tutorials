#!/bin/env python

s = "Welcome to USP 32547"

print(s)
length = len(s)
print(f'Length of s is {length}')
print("First = ",s[0])
print("Last = "+s[length-1])

s2 = s[10:]
print(s2)

s3= s[5:15]
print(s3)

print(s.lower())
print(s.upper())

print(s.count("o"))

s4= s.replace("Welcome to","Subject")
print(s4)

print("m is at position: ",s.find("m"))
print("m is at position: ",s.index("m"))


print("USP32547".isalnum())









