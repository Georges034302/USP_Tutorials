#!/bin/env python3

import utils as u

def main():
    nums = u.generate(int(u.read("First = ")), int(u.read("Last = ")), int(u.read("Size = ")))
    print(nums)
    mean, var, stdv = u.liststats(nums)
    print("Mean = %d, Variance = %f, Stdv = %.2f "%(mean,var,stdv))
    keys = u.generate(1,99,3)
    print("Keys --->"+str(keys))
    names = u.createdict(keys)
    u.sort(names)

main()
