#!/bin/env python3

import random as r
import statistics as stat 

def read(action):
    return input(action)

def generate(first,last,howmany):
    return r.sample(range(first,last),howmany)

def liststats(*argv):
    mean = stat.mean(*argv)
    var = stat.variance(*argv)
    stdv = stat.stdev(*argv)
    return mean, var, stdv

def createdict(argv):
    names = {}
    keys = argv
    for key in keys:
        names[key] = read("Name = ")
    return names

def sort(dicts):
    for key in sorted(dicts.keys()):
        print("%s --> %s"%(key,dicts[key]))
