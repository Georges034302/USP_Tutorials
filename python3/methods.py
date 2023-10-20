#!/bin/python3
import math 

def move(distance):
    pos = 0
    pos += distance
    print(pos)

move(10)
move(20)

def distance(speed, time):
    return speed * time 

d = distance(40,5)
print(d)

def geometry(r):
    p = 2*math.pi*r
    a = math.pi*pow(r,2)
    v = (4/3)*math.pi*math.pow(r,3)
    return p, a, v 

p, a, v = geometry(4)
print(f'Perimeter = {p:.2f}')
print(f'AREA = {a:.3f}')
print(f'VOLUME = {v:.4f}')


