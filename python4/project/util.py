#!/usr/bin/env python3
import math
import statistics as stat
import random as  ran

def read(action):
    return input(action+": ")

def circle(radius):
    perimeter = 2*math.pi*float(radius)
    area = math.pi*math.pow(float(radius),2)
    sarea = 4*math.pi*math.pow(float(radius),2)
    svolume = (4/3)*math.pi*math.pow(float(radius),3)
    return perimeter, area, sarea, svolume

def randomlist(first,last,howmany):   
    return ran.sample(range(first,last),howmany)        

def liststats(list):
    mean = stat.mean(list)
    var = stat.variance(list)
    stdv = stat.stdev(list)
    s = sum(list)
    return mean, var, stdv, s

#Create
def createdict():
    names = {}
    keys = ran.sample(range(100,1000),4)
    for key in keys:
        names[key] = read("Name")
    return names

#Read
def printdict(dict):
    for key in sorted(dict.keys()):
        print("%2s :: %s "% (key,dict[key]))

#Update
def update(dict, key, value):
    dict[key] = value

#Delete
def delete(dict, key):
    del dict[key]












