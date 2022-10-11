#!/bin/env python

import random as r 

def read(prompt):
    return input(prompt)

def generate(first,last,size):
    return r.sample(range(first,last),size)

def show(*argv):
    print(*argv)

def find(target, numbers):
    for e in numbers:
        if(e == target):
            return True
    return False


