#!/bin/env python3
#Define a script that:
#Read an integer n from stdin
#determine the square of n
#Determine the sum-series of n
#Determine the factorial of n
#NOTE: Every program must have a main funtion 

def read_n():
    return int(input("N = "))

def square_n(n):
    f = lambda x: pow(x,2) # f = f(x) = x**2
    return f(n)

#Recursive add series
def add_n(n):   
    f = lambda x: x + f(x-1) if x > 0 else 0 # f = f(x) = x + f(x-1)
    return f(n)

#Recursive factorial
def factorial(n):  
    f = lambda x: x*f(x-1) if x > 0 else 1 # f = f(x) = x * f(x-1) 
    return f(n)

def main():
    n = read_n()
    print("Square({}) = {}".format(n,square_n(n)))
    print("Sum Series({}) = {}".format(n,add_n(n)))
    print("Factorial({}) = {}".format(n,factorial(n)))
main()


