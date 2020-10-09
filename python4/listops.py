#!/bin/env python3


def generate(first,last):
    return range(first,last)

## *argv represents variable number of arguments
def calculate(*argv):
    x = sum(*argv)
    average = x/len(*argv)
    m = min(*argv)
    z = max(*argv)
    return x, average, m, z

def show():
    nums = generate(3,10)
    print(nums)
    x, y, m, z = calculate(nums)
    print("SUM= "+str(x))
    print("Average= "+str(y))
    print("Min = "+str(m))
    print("Max = "+str(z))

show()
