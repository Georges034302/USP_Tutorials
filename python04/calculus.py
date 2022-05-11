#!/bin/env python3

def read(prompt):
    return input(prompt)
    
def calculate(a,b):
    return a+b,a-b,a*b,a/b,pow(a,b),a%b  

def main():
    a = int(read("a = "))
    b = int(read("b = "))
    m, n, p, q, x, y = calculate(a,b)
    print(f'{m} ; {n}, {p}, {q}, {x}, {y}')

main()
