#!/bin/python3

x = 2
y = 3

print(x == y)
print(x is y)

print(x != y)
print(x is not y)
print(not(x == y))
print(not(x is y))

z = x + 3 * y # BODMAS
print(z)

z = (x + 3) * y 
print(z)

b = (x > 2) or (x <= 2) # False or True
print(b)

b = not( x is 2) and (y > 2 or x is y)
print(b)

f = 2.0
print ( x is f)
print ( x == f)
print ( x > f )