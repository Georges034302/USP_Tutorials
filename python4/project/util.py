#!/bin/env python3
import math as m 
import statistics as stat 
import random as r 

#general read function 
def read(action):
    return input(action+": ")

#calculate area, perimeter, volume of a circle/sphere
def calculate(radius):
    perimeter = 2*m.pi*radius
    area = m.pi*m.pow(radius,2)
    volume = (4/3)*m.pi*m.pow(radius,3)
    return perimeter, area, volume 

def generate(first,last,howmany):
    return r.sample(range(first,last),howmany)

def liststats(*argv):
    mean = stat.mean(*argv)
    var = stat.variance(*argv)
    stdv = stat.stdev(*argv)
    s = sum(*argv)
    return mean,var,stdv,s

def createdict():
    names={}
    keys = r.sample(range(100,1000),4)
    for key in keys:
        names[key] = read("Name")
    return names

def sort(dicts):
    for key in dicts.keys():
        print("%s :: %s"%(key,dicts[key]))

def update(dicts,key,newvalue):
    dicts[key] = newvalue

def delete(dicts,key):
    del dicts[key]





























