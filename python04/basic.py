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
    return n**2

def add_n(n):
    s = 0
    for e in range(1,n+1):
        s += e
    return s

def factorial(n):
    f = 1
    for e in range(1,n+1):
        f *= e
    return f

def main():
    n = read_n()
    print("Square({}) = {}".format(n,square_n(n)))
    print("Sum Series({}) = {}".format(n,add_n(n)))
    print("Factorial({}) = {}".format(n,factorial(n)))
main()


