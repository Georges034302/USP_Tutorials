#!/bin/env python

x = 2
y = 3

print(x is y)
print(x is not y)

print(x < y)
print(x <= y)

test2 = x < y

print(not(test2))

test = (x is y) or (x is not y)
print("Test --> ",test)

test = (x is y) and (x is not y)
print("Test --> ",test)

test = not(x is y) and (x < y)
print("Test --> ",test)

test = not(x is y) and (x == y)
print("Test --> ",test)

test = (x is not y) and (x != y)
print("Test --> ",test)
