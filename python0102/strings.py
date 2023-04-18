#!/bin/python3

s = "USP 32547 Python"
#String is ordered, indexed
length = len(s) # return the length of a string

print("Length = "+str(length))
print("Length = ",length) # will join an int to str with a space

print("First = "+s[0])
print("Last = "+s[len(s)-1])
print("Slice(1 to 3): "+s[0:3]) # s[a:b] a included and b excluded
print("Right side: "+s[int(length/2):])

print(s.lower())

print(s.replace("P","_"))
s2 = s.replace("Python","Java")
print(s2)

print(s2.count('a')) # counting the occurence of a character in a string

print(s2.index('a')) # index returns the position of the first charcater occurence in a string
print(s2.find('a')) # same as index

print(s2.isalpha())
print(s2.isalnum())