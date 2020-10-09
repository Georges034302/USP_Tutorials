#!/bin/env python3
#Generate a list of integers
#calculate:
#sum
#average
#min
#max

import random as r

def generate(first,last,howmany):
    return list(r.sample(range(first,last),howmany))

def calculate(*argv):
    s = sum(*argv)
    average = s/len(*argv)
    m = min(*argv)
    z = max(*argv)
    return s,average, m, z

def main():
    nums = generate(1,40,10)
    print(nums)
    x, y, m , z = calculate(nums)
    print("Sum = "+str(x))
    print("Average = "+str(y))
    print("Min = "+str(m))
    print("Max = "+str(z))

main()
