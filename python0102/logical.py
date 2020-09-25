#!/bin/env python3

x = y = "hello"
print(x)
print(y)
print (x is y)

print("----------------------------")
x, y = 6, "hello"
print(x)
print(y)
print (x is y)
print (not(x is y))
print (x is not y)

print("----------------------------")
x, y = 3, 3
print(x)
print(y)
print (x == y)
print (x != y)
print (x > y)
print (x < y)
print (x >= y)
print (x <= y)

print (not (x==y))
print ((x!=y) or (x > 1))
print ((x!=y) and (x > 1))

