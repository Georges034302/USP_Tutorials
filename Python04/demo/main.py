#!/bin/env python3

import utils as u 

def circleOps():
    r = int(u.read("Radius"))
    p, a, v = u.calculate(r)
    u.show("Perimeter = {:.2f}".format(p))
    u.show("Area = {:.3f}".format(a))
    u.show("Volume = {:.3f}".format(v))

def listOps():
    values = u.generate(1,100,10)
    m, v, std, s = u.listStats(values)
    u.show(values)
    u.show("Mean = {:.2f}".format(m))
    u.show("Variance = {:.3f}".format(v))
    u.show("Standard deviation = {:.2f}".format(std))
    u.show("Sum = {}".format(s))

def main():
    circleOps()
    listOps()

main()
