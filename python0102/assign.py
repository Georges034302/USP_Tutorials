#!/bin/env python3

x = y = z = "hello"
print(x)
print(y)
print(z)
print("----------------------------")
x, y, z = 5, 6, "hello"
print(x)
print(y)
print(z)
print("----------------------------")
x, y, z = 5, 3, 2
print(x)
print(y)
print(z)
print("----------------------------")
y+=x
print(y)
y-=x
print(y)

z*=(1+1j)
print(z)
z /= 1j
print(z)

x = 5
x **=2
print(x)

x = 5
x/=2
print(x)
print(int(x))

x = 5
x//=2
print(x)

x = 5
x%=2
print(x)

