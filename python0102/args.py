#!/bin/env python3
#Detect the script arguments and apply the follwing scenarios:
#if zero argument exists then print a message
#if one argument exists the print that argument
#if many arguments exist then print the argument list

import sys

length=len(sys.argv)

if (length == 1) :
    print(sys.argv[0]+" has no arguments!")
elif (length == 2):
    print(sys.argv[0]+"has argument: "+sys.argv[1])
else:
    print("Argument list: "+str(sys.argv))


