#!/bin/env python

x = 2
y = 3

x = x + 1 # add 1 to the original value of x and then store it into x
print(x)

x += 1
print("x = ",x)

y -=2 # y = y -2
print(y)

y += x # y = y + x
print("y = ",y)

#power of x by 2
print(x**2)
print(pow(x,2))

print("y/2 = %.3f"%(y/2))
s = "y/2 = {:.2f}".format(y/2)
print(s)

print(f'y/2 = {y/2:.5f}')

print(y % 2)
