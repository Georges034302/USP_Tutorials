#!/bin/env python3

def read_n():
    return int(input("n = "))

#Square 2
def square(n):     
    return n**2

#Add-Series n 
def add(n):
    s = 0
    for i in range(1,n+1):
        s+= i
    return s

#Factorial n
def factorial(n):
    f = 1
    for i in range(1,n+1):
        f *= i
    return f

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



