#!/bin/env python3
#Read n from user-input
#Define a function to sqaure n 
#Define an Add-Series (n) means: 1+2+3+....+n
#Define a factorial function (n), means: 1*2*3*...*n
#Define a main function to run the script and ensure it runs until -1

def read_n():
    return int(input("N = "))

def square(n):
    s = lambda x: pow(x,2)
    return s(n)

#Using Recursion to add all numbers from n to 1
def add(n):
    s = lambda x: x+s(x-1) if x > 0 else 0
    return s(n)       

#Using Recursion to multiply all numbers from n to 1
def factorial(n):
    fac = lambda x: x*fac(x-1) if x > 0 else 1
    return fac(n)
    
def main():
    n = read_n()
    while n!= -1:
        print("Square ("+str(n)+") = "+str(square(n)))
        print("Add-S ("+str(n)+") = "+str(add(n)))
        print("Factorial ("+str(n)+") = "+str(factorial(n)))
        n = read_n()

main()


