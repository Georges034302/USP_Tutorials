#!/bin/env python3
import random as r 

def generate(first,last,howmany):
    return r.sample(range(first,last),howmany)


def calculate(*argv):
    s = sum(*argv)
    a = s/len(*argv)
    m = min(*argv)
    z = max(*argv)
    return s, a, m, z

def main():
    nums = generate(5,50,10)
    s, a, m, z = calculate(nums)
    print(nums)
    print("Sum = "+str(s))
    print("Ave = {:.3f}".format(a))
    print("Min = "+str(m))
    print("Max = "+str(z))

main() 

