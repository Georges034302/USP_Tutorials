#!/bin/env python3
#Define a script that detects how many arguments you pass to a script

import sys

length=len(sys.argv)

if (length == 1):
    print(sys.argv[0]+" has not arguments!")
elif (length == 2):
    print(sys.argv[0]+" has one arguments!: "+sys.argv[1])
else:
    print(sys.argv[0]+" has the following arguemts: "+str(sys.argv))
