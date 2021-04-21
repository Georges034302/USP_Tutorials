#!/bin/env python3
s = "Subject USP 32547"

length = len(s)
print("String: "+s)
print("Length of s = "+str(length))
print()
print(">>> Accessing string characters:")
print("First character: "+s[0])
print("last chracter: "+s[length-1])
print("Substring: "+s[12:length])
print("Reverse: "+s[-10:-6])
print()
print(">>> String functions:")
print(s.lower())
print(s.upper())
print(s.count("S"))
print(s.split(" "))
print(s.replace("USP","Python"))
print(s.replace("P","D"))
print(s.find("USP"))
print(s.find("S"))
print(s.isalpha())
print(s.isalnum())
print("USP32547".isalnum())
print(s.isdigit())
print(s[12:length].isdigit())
print(s.index("3"))





