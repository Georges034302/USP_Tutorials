#!/bin/env python

# Read in the radius of a compile
# Calculate and return: perimeter, area, and volume
# Define the main method that prints the above values
import math as m 

def read(prompt):
    return input(prompt)

def calculate(radius):
    perimeter = 2 * m.pi * radius 
    area = m.pi * m.pow(radius,2)
    volume = (4/3) * m.pi * pow(radius,3)
    return perimeter, area, volume

def main():
    radius = float(read("Radius = "))
    p, a, v = calculate(radius)
    print(f'Perimeter = {p:.2f}')
    print(f'Area = {a:.3f}')
    print(f'Volume = {v:.4f}')
main()
