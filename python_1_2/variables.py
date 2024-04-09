#!/bin/env python3

# Initializing script variables
x = 2
print(type(x))
b = True
print(type(b))
y = 3.5
print(type(y))

result1 = x + b
print(result1)

result2 = x + y 
print(result2)

result3 = x**3
print(result3)
result4 = pow(x,4)
print(result4)

result5 = x * 4 + y #11.0
print(result5)

result6 = x *(4 + y) #15.0
print(result6)

# Joining output values
# print output strings
# + joins (concatunate) strings only
print('x = '+str(x))

# print can evaluate and print boolean value as string
print(x < y)
print(x == x)
print(x is x)
print(x is not x)
print(x != x)

b = (x >= x) and (y is not y)
print(b)

b = (x+2 < y) or not(x == x) 
print(b)







