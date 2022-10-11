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
    return pow(n,2)

def sumSeries(n):
    return sum(range(1,n+1))

def factorial(n):    
    return m.factorial(n)

def main():
    n = int(read("N = "))
    print(f'Square({n}) = {square(n)}')
    print(f'Sum Series({n}) = {sumSeries(n)}')
    print(f'Factorial({n}) = {factorial(n)}')
    
main()
