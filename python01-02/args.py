#!/bin/env python3
#Detect the script arguments and apply the following scenarios:
#1 - if zero arguments then print a message
#2 - if we have 1 argument then print that argument 
#3 - if we have many arguments then print the argument list 

import sys

length = len(sys.argv)

#if <logical condition>:
#   <code>

if(length == 1): 
    print(sys.argv[0]," has no arguments!")
elif length == 2:
    print(sys.argv[0]," has the argument: ",sys.argv[1])
else:
    print("Argument list: ",sys.argv)
