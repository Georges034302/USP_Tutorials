#!/bin/env python3

def read_n():
    return int(input("n = "))

#Square n
def square(n):
    s = lambda x: pow(x,2)
    return s(n)

#Add-Series
def add(n):
    s = lambda x: x+s(x-1) if x>0 else 0
    return s(n)

#Factorial n
def factorial(n):      
    fac = lambda f: f*fac(f-1) if f>0 else 1  
    return fac(n)

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
