#!/bin/env python3

nums = list(range(1,20))


def calculate(nums):
    x = sum(nums)
    average = x/len(nums)
    m = min(nums)
    z = max(nums)
    return x, average, m, z

def show():
    print(nums)
    x, y, m, z = calculate(nums)
    print("SUM= "+str(x))
    print("Average= "+str(y))
    print("Min = "+str(m))
    print("Max = "+str(z))

show()
