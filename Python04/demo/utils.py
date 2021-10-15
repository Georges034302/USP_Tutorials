#!/bin/env python3

import math as m 
import random as r 
import statistics as stat

#read function
def read(action):
    return input(action+" = ")

#output function
def show(out):
    print(out)

#define a function that calculates: peremiter, area, volume for a given radius
def calculate(radius):
    p = m.pi*2*radius  
    a = m.pi*m.pow(radius,2)
    v = (4/3)*m.pi*m.pow(radius,3)
    return p, a, v

#define a function that generates a random sample (n) from first to last
def generate(first,last,n):
    return r.sample(range(first,last+1),n)

#calculate the mean, variance, standard deviation, sum of a list
def listStats(*argv):
    mean = stat.mean(*argv)
    var = stat.variance(*argv)
    stdv = stat.stdev(*argv)
    s = sum(*argv)
    return mean, var, stdv, s


