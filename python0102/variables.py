#!/bin/env python3

d = 5
s = "Tim"
b = True
f = 2.33
c = 1+1j

#types
print(d, end=" is: "+str(type(d))+"\n")
print(f, end=" is: "+str(type(f))+"\n")
print(b, end=" is: "+str(type(b))+"\n")
print(c, end=" is: "+str(type(c))+"\n")
print(s, end=" is: "+str(type(s))+"\n")

#casting
print(int(f))
print(int(b))
print(int(False))

print(float(d))
print(float(b))
print(float(False))

print(bool(d))
print(bool(s))
print(bool(c))
print(bool(f))

print(str(d))
print(str(f))
print(str(b))
print(str(c))

print(complex(d))
print(complex(f))
print(complex(b))
print(complex(False))

