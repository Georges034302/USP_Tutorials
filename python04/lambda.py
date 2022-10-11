#!/bin/env python

# Read an integer n from STDIN
# Define a function that returns the square of n
# Define a function that returns the sum-series of n
# Define a function that returns the factorial of n 
# Define a function main() that shows the results
import math as m 

def read(prompt):
    return input(prompt)

def square(n):
    P = lambda x: pow(x,2)
    return P(n)

def sumSeries(n):
    S = lambda x: x + S(x-1) if x > 1 else 0
    return S(n)

def factorial(n):  
    F = lambda x: x * F(x-1) if x > 1 else 1  
    return F(n)

def main():
    n = int(read("N = "))
    print(f'Square({n}) = {square(n)}')
    print(f'Sum Series({n}) = {sumSeries(n)}')
    print(f'Factorial({n}) = {factorial(n)}')
    
main()
