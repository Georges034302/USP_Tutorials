#!/bin/env python3

#read function
def read_n():
    return int(input("N = "))

#output function
def show(n):
    print(n)

#define a function that returns the square of N
def square(n):
    s = lambda x: pow(x,2)
    return s(n)

#Define a function that adds a range of n values
def add(n):  
    s = lambda x: x+s(x-1) if x > 0 else 0 
    return s(n)

#Define a factorial function of N 
def factorial(n):
    f = lambda x: x*f(x-1) if(x > 0) else 1
    return f(n)

#calling functions after the definition
def main():
    n = read_n()
    show("Square("+str(n)+") = "+str(square(n)))
    show("Sum Series("+str(n)+") = "+str(add(n)))
    show("Factorial("+str(n)+") = "+str(factorial(n)))

main()
