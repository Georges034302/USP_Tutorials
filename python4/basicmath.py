#!/bin/env python3
#Read n from user-input
#Define a function to sqaure n 
#Define an Add-Series (n) means: 1+2+3+....+n
#Define a factorial function (n), means: 1*2*3*...*n
#Define a main function to run the script and ensure it runs until -1

def read_n():
    return int(input("N = "))

def square(n):
    return n**2

def add(n):
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
    while n!= -1:
        print("Square ("+str(n)+") = "+str(square(n)))
        print("Add-S ("+str(n)+") = "+str(add(n)))
        print("Factorial ("+str(n)+") = "+str(factorial(n)))
        n = read_n()

main()


