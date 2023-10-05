#!/bin/python3

x = 2
y = 3

print(x == y)
print(x is y)

print(x is not y)
print(x != y)

print(not(x == y))

b = (x < y) or (not x) and (x > y)
print(b)

b = (x < y or x > 5) and not(x == y)
print(b)
