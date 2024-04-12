#!/bin/env python3

x = 2       # this is an integer
y = 2.5     # this is a float 
z = True    # this is a boolean

print(type(x))

print(x+y)
print(x+z)

result1 = x**2
print(result1)

result2 = pow(x,2)
print(result1)

result3 = x * 2 + y 
print(result3)

result4 = x * (2+y)
print(result4)

b = (x <= y) or (x is not x)
print(b)

b = (x != y) and not(x+1 > y)
print(b)

b = (x is x) and not(y == y)
print(b)






