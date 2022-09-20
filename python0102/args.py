#!/bin/env python

import sys 

length = len(sys.argv)

if(length == 1):
    print(sys.argv[0]+" has no arguments")
elif (length == 2):
    print(sys.argv[0]+" has one argument: "+sys.argv[1])
else:
    print("Argument list: "+str(sys.argv))
