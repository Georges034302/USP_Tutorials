#!/bin/env python3
#Capture arguments and determine what arguments and how many 

import sys

length = len(sys.argv) #buffer array that stores arguments temporarly

if(length == 1):
    print(sys.argv[0]+" has no arguments") # similar to $0 in bash
elif (length == 2):
    print(sys.argv[0]+" has argument "+sys.argv[1])
else:
    print("Argument list: "+str(sys.argv))
