#!/bin/env python3

#Functions in Python are not hoisted (you can only call a function below the definition)
#def function_name(paramters):
#    <some code >
#    <optional return>

#to execute call the function as follows: function_name(arguments)

#read function
def read_n():
    return int(input("N = "))

#output function
def show(n):
    print(n)

#define a function that returns the square of N
def square(n):
    return n**2

#Define a function that adds a range of n values
def add(n):
    s = 0
    for e in range(1,n+1):
        s += e  
    return s

#Define a factorial function of N 
def factorial(n):
    f = 1
    for e in range(1,n+1):
        f *= e
    return f

#calling functions after the definition
def main():
    n = read_n()
    show("Square("+str(n)+") = "+str(square(n)))
    show("Sum Series("+str(n)+") = "+str(add(n)))
    show("Factorial("+str(n)+") = "+str(factorial(n)))

main()





