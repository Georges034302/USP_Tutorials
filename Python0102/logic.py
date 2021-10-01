#!/bin/env python3

x = y = "hello"
print(x is y)

x , y = 5, "hi"
print(x is y)
print(not(x is y)) #inversing the previous result
print(x is not y)  #checking if x is not equal to y


x = y = 3

print(x == y)
print(not(x == y))
print(x != y) #similar to print(not(x is y))
print(x > y)
print(x >= y)

exp1 = ((x != y) or (x > 1))
print(exp1) 

exp2 = ((x != y) and (x > 1))
print(exp2) 
