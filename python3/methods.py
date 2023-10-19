#!/bin/python3
import math as m
# Method:
# 1- Procedure:
#   - method with no return Value
#   - is an action
#   - verb

# 2- Functions:
#   - method with a return value 
#   - is a noun 
#   - can be assigned into a variable

def move(distance):
    global position
    position = 10
    position += distance + 10
    print(position)

move(10)

def distance(speed,t):
    return speed * t 

d = distance(40,5)
print(f'distance travelled = {d}')

def geometry(r):
    p = 2* m.pi*r 
    a = m.pi*pow(r,2)
    v = (4/3)*m.pi*m.pow(r,3)
    return p, a, v 

r = 3

p, a, v = geometry(3)
print(f'Perimeter = {p:.3f}')
print(f'area = {a:.2f}')
print(f'volume {v:.4f}')










