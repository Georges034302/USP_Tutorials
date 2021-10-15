#!/bin/env python3

import math as m 

#read function
def read_n():
    return int(input("N = "))

#output function
def show(n):
    print(n)

#define a function that returns the square of N
def square(n):
    return int(m.pow(n,2))

#Define a function that adds a range of n values
def add(n):    
    return sum(range(1,n+1))

#Define a factorial function of N 
def factorial(n):
    return m.factorial(n)

#calling functions after the definition
def main():
    n = read_n()
    show("Square("+str(n)+") = "+str(square(n)))
    show("Sum Series("+str(n)+") = "+str(add(n)))
    show("Factorial("+str(n)+") = "+str(factorial(n)))

main()
