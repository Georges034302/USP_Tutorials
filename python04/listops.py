#!/bin/env python3
#Define a script that:
#generates a random list 
#caculates the sum,length,average, min,max values in the list 

import random as r 

def read_n(prompt):
    return int(input(prompt))

def generate(first,last,howmany):
    return r.sample(range(first,last),howmany)

def calculate(*argv):
    s = sum(*argv)
    l = len(*argv)
    a = s/l
    m = min(*argv)
    x = max(*argv)
    return s, l, a, m, x

def main():
    nums = generate(read_n("First = "),read_n("Last = "), read_n("Size = "))
    print("Random list --> "+str(nums))
    s, l, a, m, x = calculate(nums)
    print("Sum = {}, Length = {}, Average = {}, Min = {}, Max = {}".format(s,l,a,m,x))
main()
