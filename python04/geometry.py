#!/bin/env python3
#For a radius r (from STDIN) calculate the following:
# 1- perimeter of the circle  
# 2- area of a disk
# 3- volume of a sphere
import math as m

def read(prompt):
    return input(prompt)
    
def calculate(r):
    perimeter = 2*r*m.pi
    area = m.pi*pow(r,2)
    volume = (4/3)*m.pi*pow(r,3)
    return perimeter, area, volume

def main():
    radius = float(read("Radius: "))
    p, a, v = calculate(radius)
    print(f'perimeter= {p:.2f}; area = {a:.3f}; volume = {v:.4f}')


main()
