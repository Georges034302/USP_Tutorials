#!/bin/env python3

def factorial(n):      
    fac = lambda f: f*fac(f-1) if f>0 else 1  
    return fac(n)

def read_n():
    return int(input("n = "))

def main():    
    n=read_n()
    while n != -1:
        print("Facotorial "+str(n)+" = "+str(factorial(n)))
        n=read_n()

main()
