#!/bin/env python3
import math as m 

def read_n():
    return int(input("n = "))

#Square 2 
def square(n):
    return int(m.pow(n,2))

#Add-series n 
def add(n):   
    return sum(range(1,n+1))

#Factorial n
def factorial(n):    
    return m.factorial(n)

#Main function
def main():    
    n=read_n()
    while n != -1:
        print("Square("+str(n)+") = "+str(square(n)))
        print("Sum("+str(n)+") = "+str(add(n)))        
        print("Facotorial("+str(n)+") = "+str(factorial(n)))
        
        n=read_n()

#Invode the main function
main()
