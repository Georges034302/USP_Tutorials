#!/bin/python3
import sys

x = int(input('x = '))
print(x+2)

y = int(sys.argv[1]) # capture first argument
print(x + y)
