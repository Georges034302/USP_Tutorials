#!/bin/env python3

s = "Welcome to USP 32547"

length = len(s)

#String access
print("Length = "+str(length)+"\n")
print("First character: "+s[0])
print("Last charcater: "+s[length-1])
print("Substring: "+s[11:length])
print("Substring: "+s[11:15])
print("Reverse: "+s[-5:-2])
print()

#String functions
print(s)
print(s.lower())
print(s.upper())
print(s.count("o"))
print(s.replace("USP","Python"))
print(s.find("USP")) # index of the U 
print(s.isalpha())
print(s.isalnum())
print(s.index("U"))

print(s.split(" ")) # returns an array of words
a = s.split(" ") #store the result array into a vairable a
print(a[3])
