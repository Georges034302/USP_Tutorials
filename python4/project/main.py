#!/bin/env python3

import util as u 

def circleops():
    r = float(u.read("Radius"))
    p, a, v = u.calculate(r)
    print("Perimeter = {:.2f}".format(p))
    print("Area = {:.3f}".format(a))
    print("Volume = {:.4f}".format(v))


def liststats():
    nums = u.generate(1,100,10)
    m, v , stdv, s = u.liststats(nums)
    print(nums)
    print("Mean = "+str(m))
    print("Variance = "+str(v))
    print("Stdv = "+str(stdv))
    print("Sum = "+str(s))

def dictops():
    names = u.createdict()
    u.sort(names)
    key = int(u.read("Key"))
    value = u.read("Value")
    u.update(names,key,value)
    u.sort(names)
    key = int(u.read("Delete by Key"))
    u.delete(names,key)
    u.sort(names)

def main():
    circleops()
    liststats()
    dictops()

main()









