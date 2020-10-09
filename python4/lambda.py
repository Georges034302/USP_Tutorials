#!/bin/env python3
#Read integer from use 
#define a function to square n 
#define a function to add-series (n): 1+2+3+...+n
#define a function factorial (n): 1*2*3*...*n
#define a main function to run the script 
import math as m 

def read_n():
    return int(input("N = "))

def square(n):
    s = lambda x: pow(x,2)
    return s(n)
#Using recursion and lambda to calculate add-series of n
def add(n):
    s = lambda x: x+s(x-1) if x > 0 else 0
    return s(n)        

#Using recursion and lambda to calculate factorial of n
def factorial(n):
    f = lambda x: x*f(x-1) if x > 0 else 1
    return f(n)
        
def main():
    n = read_n()
    while n != -1:
        print("Square("+str(n)+") = "+str(square(n)))
        print("Add-S("+str(n)+") = "+str(add(n)))
        print("Facorial("+str(n)+") = "+str(factorial(n)))
        n = read_n()

main()

