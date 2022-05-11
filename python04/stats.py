#!/bin/env python3
#generate a list and select random choices from this list of size (howmany)
#calculate min, max, total of this list 
#calculate mean, variance, stdev of this list 
import random as ran 
import statistics as stat 

def read(prompt):
    return input(prompt)
    
def ranlist(first,last,step,howmany):
    return ran.sample(range(first,last,step),howmany)

def calculate(*argv):
    maximum = max(*argv)
    minimum = min(*argv)
    total = sum(*argv)
    return maximum, minimum, total

def statops(*argv):
    m = stat.mean(*argv)
    v = stat.variance(*argv)
    stdv = stat.stdev(*argv)
    return m, v, stdv

def main():
    first = int(read("First = "))
    last = int(read("Last = "))
    step = int(read("Step = "))
    size = int(read("How Many = "))
    mylist = ranlist(first,last,step,size)
    print("My random list: ")
    print(mylist)
    maximum, minimum, total = calculate(mylist)
    print("MAX = {}".format(maximum))
    print("MIN = ",minimum)
    print("TOTAL = %d"%(total))
    print("\n----------------------------------\n")
    m, v, stdv = statops(mylist)
    print(f'MEAN = {m:.2f}')
    print("Variance = {:.3f}".format(v))
    print("STDV = %.4f"%(stdv))

main()






