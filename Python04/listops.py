#!/bin/env python3

import random as r 

#define a function that generates a random sample (n) from first to last
def generate(first,last,n):
    return r.sample(range(first,last+1),n)

def calculate(*argv):
    s = sum(*argv)
    a = s/len(*argv)
    m = min(*argv)
    M = max(*argv)
    return s, a, m, M

#output function
def show(n):
    print(n)

def main():
    values = generate(5,50,8)
    s, a, m, M = calculate(values)    
    show(values)
    show("Sum = "+str(s))
    show("Average = {:.2f}".format(a))
    show("Min = "+str(m))
    show("Max = "+str(M))

main()
