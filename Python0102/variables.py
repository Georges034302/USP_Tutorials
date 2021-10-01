#!/bin/env python3

#Variable types are determine on creation

#initialize variables
a = 5
b = 2.5
c = False
d = "Welcome"
e = 2j

#Determine a type and join a type in a string output
print("Types: "+str(type(a))+" another: "+str(type(c)))

#Type conversion
print("b becomes: "+str(int(b))+" and a becomes: "+str(complex(a)))

#Other ways of initialize variables
x = y = z = "hello"
print(x,end="-"+y+"\n")

x, y, z = 5, 6, "hello"
print(str(x+y)+"-"+z+"\n")

x = x + 1
print(x)
x += 1
print(x)
x -= 2
print(x)
x = x -1
print(x)

#now x  is 4
x **=2
print(x)

#now x is 16
x %=3
print(x)














