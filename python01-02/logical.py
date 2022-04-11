#!/bin/env python3 

x = 2
y = 3

print(x is y)
print(x == y)
print(x is not y)
print(not(x is y))
print(not(x == y))
print(x != y)

x, y, z = 2, "Hi", 2.5
print(x,y,z)

x = y = z = 2
print(x,y,z)

x, y, z = 2, 4, 2
print(x < y)
print(x > z)
print(x >= z)
print(x != y)

b = ((x != z) or not(z < y))
print(b)

b = ((x == z) or not(z < y))
print(b)

b = ((x == z) and not(z < y))
print(b)




